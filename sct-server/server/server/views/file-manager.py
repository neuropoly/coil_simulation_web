import os, zipfile, logging
import io
import re
from ..cfg import FILE_REP_TMP
from cornice import Service
import jsonpickle
from server.models import models
from pyramid import response
import zlib
#####
# AngularJS - File Tree
#####

tree_desc = " ''' Service that read the database to generate a tree for a specific user'''"

tree = Service('tree',
                '/tree',
               tree_desc)

def path_to_db(path,session,tag):
    '''
    :param path: the path where to scan files and folders
    :param session: the SQL session.db
    :param tag: a tag to identify the first iteration of the recursive loop as the root folder/file
    :return: Register each file and each folder into the database, recursively
    '''
    if os.path.basename(path).find("deleted")<0:
        d = {'text': os.path.basename(path)}
        d['path'] = path #The absolute path, usefull to launch the SCToolbox
        d['rel_path'] = re.match(".*server/server/(static.*)", path).groups()[0]
        #d['rel_path'] = os.path.relpath(path)[52:] #The relative path, usefull to load volumes files into BrainBrowser
        if tag:
            d['parent'] = "#"
            d['state'] = '{"opened" : true, "selected" : false, "disabled"  : true }'
            d['icon'] = "glyphicon glyphicon-user"
        else :
            d['parent'] = os.path.abspath(os.path.join(path, os.pardir))
            d['state'] = '{"opened" : false,"selected" : false, "disabled"  : false }'
        if os.path.isdir(path):
            d['type'] = "directory"
            d['children'] = [path_to_db(os.path.join(path,x),session,0) for x in os.listdir(path)]
            if tag is 0:
                d['icon'] = "glyphicon glyphicon-folder-open"
        else:
            d['type'] = "file"
            if tag is 0:
                d['icon'] = "glyphicon glyphicon-file"
            d['children'] = ""

        logging.info(d['parent'])
        u = models.tree(rel_path = d['rel_path'],
                        size = 0,
                        text = d['text'],
                        type = d['type'],
                        id = d['path'],
                        parent = d['parent'],
                        icon = d['icon'],
                        state = d['state']
                        )

        session.add(u)
        session.commit()

        return d

@tree.get()
def tree_get(request):
    '''
    :param request.uid: The uid of the active user
    :return: a JSON with all the files and folders of the user in order to generate the file tree
    '''
    uid = str(request.unauthenticated_userid)
    session = request.db
    session.query(models.tree).delete()
    files = path_to_db(os.path.abspath(os.path.join(FILE_REP_TMP,uid)),session,1)
    fileTree = session.query(models.tree).all()
    filesT = []
    for file in fileTree:
        fileT = {'id': file.id}
        fileT['parent'] = file.parent
        fileT['icon'] = file.icon
        fileT['type'] = file.type
        fileT['path'] = file.id
        fileT['text'] = file.text
        fileT['rel_path'] = file.rel_path
        fileT['state'] = jsonpickle.loads(file.state)

        filesT.append(fileT)

    return filesT


@tree.post()
def tree_post(request):
    '''
    Post the new file tree and do the modification on the server side
    :param request:
    :return: the updated file tree
    '''
    return {}


download = Service('download',
                 '/download',
                 'Download a file or a folder')

#@TODO: a transformer en POST pour ajouter la vérification de l'utilisateur
#Les args seront: uid, file_path(s)
@download.get()
def download_get(request):
    '''
    :param request.file_id: an array of the selected files
    :return: a ziped file with all the selected files
    '''
    file_id = jsonpickle.loads(request.GET['id'])
    #test if the get argument is in the right format
    if type(file_id)==type([]):
        zip_filename = "isct_download.zip"
        # The zip compressor
        zf = zipfile.ZipFile(zip_filename, "w")
        for fpath in file_id:
            # Add files, rename it and add compression (zipfile.ZIP_DEFLATED)
            zf.write(fpath, arcname=os.path.basename(fpath), compress_type=zipfile.ZIP_DEFLATED)
        # Must close zip for all contents to be written
        zf.close()
        #TODO fix the file response, should have a real file not just the name of the zipfile in the root
        return response.FileResponse("isct_download.zip", request=request, cache_max_age=3000)
    else:
        return {'error':'argument error'}

@download.post()
def download_post(request):
    '''
    :param request.file_id: an array of the selected files
    :return: a ziped file with all the selected files
    '''
    files_id = request.json_body['files_id']
    user_id = request.json_body['uid']
    auth_id = request.unauthenticated_userid

    if type(files_id)==type([]):
        zip_filename = "isct_download.zip"
        # The zip compressor
        zf = zipfile.ZipFile(zip_filename, "w")
        for fpath in files_id:
            # Add files, rename it and add compression (zipfile.ZIP_DEFLATED)
            zf.write(fpath, arcname=os.path.basename(fpath), compress_type=zipfile.ZIP_DEFLATED)
        # Must close zip for all contents to be written
        zf.close()
        #TODO fix the file response, should have a real file not just the name of the zipfile in the root
        return response.FileResponse("isct_download.zip", request=request, cache_max_age=3000, content_type='application/zip')
    else:
        return {'error':'argument error'}

    # #test if the get argument is in the right format
    # if type(file_id)==type([]):
    #     zip_filename = "isct_download.zip"
    #     # The zip compressor
    #     zf = zipfile.ZipFile(zip_filename, "w")
    #     for fpath in file_id:
    #         # Add files, rename it and add compression (zipfile.ZIP_DEFLATED)
    #         zf.write(fpath, arcname=os.path.basename(fpath), compress_type=zipfile.ZIP_DEFLATED)
    #     # Must close zip for all contents to be written
    #     zf.close()
    #     #TODO fix the file response, should have a real file not just the name of the zipfile in the root
    #     return response.FileResponse("isct_download.zip", request=request, cache_max_age=3000)
    # else:
    #     return {'error':'argument error'}


delete = Service('delete',
                 '/delete',
                 'Mark a file or a folder as deleted')
@delete.post()
def delete_post(request):
    '''
    Delete a selected file or folder with a user verification
    :return: void
    '''
    files_id = request.json_body['files_id']
    user_id = request.json_body['uid']
    session = request.db
    #This is a verification to be sur the user is the ower of the files
    if user_id == request.unauthenticated_userid:
        for file_id in files_id:
            #Find the file in the database
            file_to_delete = session.query(models.tree).filter_by(id=file_id).first()
            #Delete the entry
            print(file_to_delete.id)
            os.rename(file_to_delete.id, (os.path.splitext(file_to_delete.id)[0]+"_deleted")+os.path.splitext(file_to_delete.id)[1])
            session.commit()
    return {}
