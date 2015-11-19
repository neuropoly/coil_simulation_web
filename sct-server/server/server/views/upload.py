import logging
import os
import uuid
import shutil
from pyramid.response import Response
from ..models import models
# from ..forms import form_render
from ..cfg import FILE_REP_TMP
import gzip

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from cornice import Service

# #@TODO: prevent symlink attacks (with token)
#
# @view_config(route_name='upload',
#              renderer='upload.mako',
#              permission='user')
# def upload(request):
#     try:
#         filename = request.POST['file'].filename
#         logging.info(filename)
#     finally:
#         return {}

# #FetchFile
# resource = Service('resource',
#                  '/resource',
#                  'Fetch the content of a txt file')
#
# @resource.get()
# def resource_get(request):
#     return {'resource':request.GET['resource']}


#UploadFile
upload = Service('upload',
                 '/upload',
                 'manage file upload')

@upload.get(renderer='upload.mako')
def upload_get(request):
    return {}

@upload.post()
def upload_post(request):
    userid = request.unauthenticated_userid #return the user.id without doing again the identification process
    userid = request.POST['username']
    # Make a directory for the current user
    try:
        os.mkdir(os.path.join(FILE_REP_TMP,str(userid)))
    except FileExistsError:
        logging.error('The folder already exist.')

    filename = request.POST['file'].filename
    file_ext = os.path.splitext(filename)[1]

    # ``input_file`` contains the actual file data which needs to be
    # stored somewhere.
    input_file = request.POST['file'].file


    if file_ext == '.nii' or file_ext == '.gz':
        file_path = os.path.join(os.path.join(FILE_REP_TMP,str(userid)), filename)

        # We first write to a temporary file to prevent incomplete files from
        # being used.
        temp_file_path = file_path + '~'

        # Finally write the data to a temporary file
        input_file.seek(0)
        with open(temp_file_path, 'wb') as output_file:
            shutil.copyfileobj(input_file, output_file)

        # Now that we know the file has been fully saved to disk move it into place.
        os.rename(temp_file_path, file_path)
        input_file.seek(0)
        size = len(input_file.read())
        #this can be an option to unizp files
    # elif file_ext == '.gz':
    #     logging.info("It's a Gzip file, let's unzip it!")
    #     filename = os.path.splitext(filename)[0] # To delete the .gz extension in the file name
    #     file_path = os.path.join(os.path.join(FILE_REP_TMP,str(userid)), filename)
    #     # We first write to a temporary file to prevent incomplete files from
    #     # being used.
    #     temp_file_path = file_path + '~'
    #
    #     #extract the file from the gzip
    #     input_file.seek(0)
    #     unzip_input_file = gzip.open(input_file, 'rb')
    #
    #     # Finally write the data to a temporary file
    #     unzip_input_file.seek(0)
    #     with open(temp_file_path, 'wb') as output_file:
    #         shutil.copyfileobj(unzip_input_file, output_file)
    #
    #     # Now that we know the file has been fully saved to disk move it into place.
    #     os.rename(temp_file_path, file_path)
    #     unzip_input_file.seek(0)
    #     size = len(unzip_input_file.read())
    #
    #     file_ext = os.path.splitext(filename)[1]
    else:
        logging.warning('Your file is neither a NIFI nor a MNC file !!! ')
        return HTTPFound(location=request.route_url('upload'))

    file_path_local = 'static/tmp/'+str(userid)+'/'+ filename #@TODO: Fix that - Dirty but will be deleted soon...

    session = request.db

    u = models.File(filename = os.path.splitext(filename)[0],
                    serverpath = file_path_local,
                    localpath=file_path_local,
                    type = file_ext,
                    user_id = userid,
                    size = size
                    )
    session.add(u)
    session.commit()
    #@TODO: Ajouter la ré-génération du tree lors d'un upload
    #return {'form':form_render,'file_path':file_path_local,'user':session.query(models.File).filter(models.File.user_id==userid).all()}
    return {}
#
# @view_config(route_name='upload_nii',
#              request_method='POST',
#              renderer='brainbrowser.mako',
#              permission='user')
# def upload_nii(request):
#     userid = request.unauthenticated_userid #return the user.id without doing again the identification process
#     # Make a directory for the current user
#     try:
#         os.mkdir(os.path.join(FILE_REP_TMP,str(userid)))
#     except FileExistsError:
#         logging.error('The folder already exist.')
#
#     filename = request.POST['files-nii'].filename
#     file_ext = os.path.splitext(filename)[1]
#
#     # ``input_file`` contains the actual file data which needs to be
#     # stored somewhere.
#     input_file = request.POST['files-nii'].file
#
#
#     if file_ext == '.nii':
#         file_path = os.path.join(os.path.join(FILE_REP_TMP,str(userid)), filename)
#
#         # We first write to a temporary file to prevent incomplete files from
#         # being used.
#         temp_file_path = file_path + '~'
#
#         # Finally write the data to a temporary file
#         input_file.seek(0)
#         with open(temp_file_path, 'wb') as output_file:
#             shutil.copyfileobj(input_file, output_file)
#
#         # Now that we know the file has been fully saved to disk move it into place.
#         os.rename(temp_file_path, file_path)
#         input_file.seek(0)
#         size = len(input_file.read())
#     elif file_ext == '.gz':
#         logging.info("It's a Gzip file, let's unzip it!")
#         filename = os.path.splitext(filename)[0] # To delete the .gz extension in the file name
#         file_path = os.path.join(os.path.join(FILE_REP_TMP,str(userid)), filename)
#         # We first write to a temporary file to prevent incomplete files from
#         # being used.
#         temp_file_path = file_path + '~'
#
#         #extract the file from the gzip
#         input_file.seek(0)
#         unzip_input_file = gzip.open(input_file, 'rb')
#
#         # Finally write the data to a temporary file
#         unzip_input_file.seek(0)
#         with open(temp_file_path, 'wb') as output_file:
#             shutil.copyfileobj(unzip_input_file, output_file)
#
#         # Now that we know the file has been fully saved to disk move it into place.
#         os.rename(temp_file_path, file_path)
#         unzip_input_file.seek(0)
#         size = len(unzip_input_file.read())
#
#         file_ext = os.path.splitext(filename)[1]
#     else:
#         logging.warning('Your file is neither a NIFI nor a MNC file !!! ')
#         return HTTPFound(location=request.route_url('upload'))
#
#     file_path_local = 'static/tmp/'+str(userid)+'/'+ filename #@TODO: Fix that - Dirty but will be deleted soon
#
#     session = request.db
#
#     u = models.File(filename = os.path.splitext(filename)[0],
#                     serverpath = file_path_local,
#                     localpath=file_path_local,
#                     type = file_ext,
#                     user_id = userid,
#                     size = size
#                     )
#     session.add(u)
#     session.commit()
#     return {'form':form_render,'file_path':file_path_local}
