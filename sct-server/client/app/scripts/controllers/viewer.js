'use strict';

/**
 * @ngdoc function
 * @name angularSeedApp.controller:ViewerCtrl
 * @description
 * # ViewerCtrl
 * Controller of the angularSeedApp
 */
angular.module('angularSeedApp')
  .controller('ViewerCtrl', function ($scope, $localStorage, $modal, getJSONcolors) {

    $scope.$storage = $localStorage;
    var volumes_files = $scope.$storage.volumes_files; //Get the volumes to load from the local storage

    //Initialize a function in order to be able to draw
    var testDraw = function (canvas_buffer, ctx, params) {
    };

    //Brush size, if == 0.5 it's deactivated
    $scope.sizeBrush = 0.5; //Brush size in 3D
    $scope.setSizeBrush = function (size) {
      $scope.sizeBrush = size;
    };
    $scope.setColorBrush = function (R,G,B) {
      $scope.color = R+","+G+","+B;
    };

    //Brush for label, if == 0.5 it's deactivated
    $scope.sizeBrushLabel = 0.5; //Brush size in 3D
    $scope.setSizeBrushLabel = function (size) {
      $scope.sizeBrushLabel = size;
    };
    $scope.addLabel = function(point){
      console.log('i:'+point.i+' j:'+point.j+' k:'+point.k);
    };


    var layer_id = 0; //volume id of the selected layer

    $scope.JSONColors = getJSONcolors.getdata();
    $scope.colorSelected = {
      "FIELD1": "0",
      "FIELD2": "Unknown",
      "FIELD3": "255",
      "FIELD4": "255",
      "FIELD5": "255",
      "FIELD6": "0"
    };
    $scope.color = $scope.colorSelected.FIELD3 + "," + $scope.colorSelected.FIELD4 + "," + $scope.colorSelected.FIELD5;
    $scope.$watch('colorSelected', function () {
      console.log($scope.colorSelected);
      //$scope.colorSelected = JSON.parse($scope.colorSelected);
      $scope.color = $scope.colorSelected.FIELD3 + "," + $scope.colorSelected.FIELD4 + "," + $scope.colorSelected.FIELD5;
    });

    //Open a modal on click with the File selector..
    $scope.open = function () {
      $modal.open({
        animation: true,
        templateUrl: '../views/browser.html',
        controller: 'BrowserCtrl'
      });
    };

    //The argument for brainbrowser to load volumes
    var load_params = {
      volumes: volumes_files
      ,
      overlay: {
        template: {
          element_id: "overlay-ui-template",
          viewer_insert_class: "overlay-viewer-display"
        },
        views: ["xspace", "yspace", "zspace"],
        canvas_layers: [
          {
            draw: testDraw
          }
        ],
        views_description: {
          "xspace": [{
            x: 0.05,
            y: 0.05,
            text: 'P'
          },
            {
              x: 0.95,
              y: 0.05,
              text: 'A'
            }],
          "yspace": [{
            x: 0.05,
            y: 0.05,
            text: 'L'
          },
            {
              x: 0.95,
              y: 0.05,
              text: 'R'
            }],
          "zspace": [
            {
              x: 0.05,
              y: 0.05,
              text: 'L'
            },
            {
              x: 0.95,
              y: 0.05,
              text: 'R'
            }
          ]
        }
      },
      complete: function () {

        $("#loading").hide();
        $("#brainbrowser-wrapper").show();
        var size = 0.75 * ($('.overlay-volume-controls').width()) / 3;
        size = size - 3.3;
        viewer.setPanelSize(size, size, {scale_image: true});
        viewer.redrawVolumes();

        viewer.volumes.forEach(function () {
          viewer.synced = true;
        });

        viewer.interaction_type = 1;
        /*
         viewer.loadVolumeColorMapFromURL(2, 'color-maps/FreeSurferColorLUT20120827.txt', "#FF0000", function() {
         viewer.redrawVolumes();
         });*/

        //Rotate panel xspace 180d
        viewer.volumes.forEach(function (volume) {
          volume.display.forEach(function (panel) {
            if (panel.axis === "xspace") {
              panel.invert_x = true;
            }
          });
        });

        // volumes_files.length : Select the overlay layer
        viewer.volumes[volumes_files.length].display.forEach(function (panel) {

          var drawPixel = function () {
            var offset = [];
            for (var i = -$scope.sizeBrush; i <= $scope.sizeBrush; i++) {
              for (var j = -$scope.sizeBrush; j <= $scope.sizeBrush; j++) {
                for (var k = -$scope.sizeBrush; k <= $scope.sizeBrush; k++) {
                  var off = [i, j, k];
                  offset.push(off);
                }
              }
            }
            var point = panel.getVoxelCoordinates();

            if (point) {

              var x = point.i;
              var y = point.j;
              var z = point.k;

              for (var i = 0; i < offset.length; i++) {
                var off = offset[i];
                viewer.volumes[layer_id].setIntensityValue(x + off[0], y + off[1], z + off[2], $scope.colorSelected.FIELD1);
              }
              viewer.redrawVolumes();
            }
          };

          var drawLabel = function () {

            var offset = [];
            for (var i = -$scope.sizeBrushLabel; i <= $scope.sizeBrushLabel; i++) {
              for (var j = -$scope.sizeBrushLabel; j <= $scope.sizeBrushLabel; j++) {
                for (var k = -$scope.sizeBrushLabel; k <= $scope.sizeBrushLabel; k++) {
                  var off = [i, j, k];
                  offset.push(off);
                }
              }
            }
            var point = panel.getVoxelCoordinates();

            if ($scope.sizeBrushLabel===0){$scope.addLabel(point);}


            if (point) {

              var x = point.i;
              var y = point.j;
              var z = point.k;

              for (var i = 0; i < offset.length; i++) {
                var off = offset[i];
                viewer.volumes[layer_id].setIntensityValue(x + off[0], y + off[1], z + off[2], $scope.colorSelected.FIELD1);
              }
              viewer.redrawVolumes();
            }
          };

          var drawMousePointer = function (x, y) {

            var volpos = panel.getVolumePosition(x, y);
            if (volpos) {
              panel.drawCurrentSlice();
              var cursorpos = panel.getCursorPosition(volpos.slice_x, volpos.slice_y);
              panel.drawMousePointer("#FFFFFF", cursorpos);
            }
          };

          var mousedown = false;

          var canvas = panel.canvas_layers[panel.canvas_layers.length - 1].canvas;

          canvas.addEventListener("mousedown", function () {
            mousedown = true;
            drawPixel();
            drawLabel();
          });

          canvas.addEventListener("mouseup", function () {
            mousedown = false;
          });

          canvas.addEventListener("mousemove", function (event) {
            var element = event.target;
            if (mousedown && !(event.ctrlKey || event.shiftKey)) {
              drawPixel();
              drawLabel();
            }
            else {
              var rect = element.getBoundingClientRect();
              drawMousePointer(event.x - rect.left, event.y - rect.top);
            }
          }, false);

        });
      }
    };

    /*
     * BrainBrowser: Web-based Neurological Visualization Tools
     * (https://brainbrowser.cbrain.mcgill.ca)
     *
     * Copyright (C) 2011
     * The Royal Institution for the Advancement of Learning
     * McGill University
     *
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU Affero General Public License as
     * published by the Free Software Foundation, either version 3 of the
     * License, or (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU Affero General Public License for more details.
     *
     * You should have received a copy of the GNU Affero General Public License
     * along with this program.  If not, see <http://www.gnu.org/licenses/>.
     */

    /*
     * Author: Tarek Sherif <tsherif@gmail.com> (http://tareksherif.ca/)
     * Author: Nicolas Kassis
     * Author: Willis Pinaud <willispinaud@gmail.com>
     */

    $(".button").button();

    /////////////////////////////////////
    // Start running the Volume Viewer
    /////////////////////////////////////
    window.viewer = BrainBrowser.VolumeViewer.start("brainbrowser", function (viewer) {
      var loading_div = $("#loading");

      ///////////////////////////
      // Set up global UI hooks.
      ///////////////////////////

      //$("#volume-type").change(function () {
      //  $("#sync-volumes-wrapper,#volume-file").hide();
      //
      //  //@TODO: delete these options but maybe add something for 4D volume?
      //  if ($(this).val() === "functional") {
      //    viewer.clearVolumes();
      //    //viewer.loadVolume({
      //    //  type: "minc",
      //    //  header_url: "scripts/brainbrowser/viewer/models/functional.mnc.header",
      //    //  raw_data_url: "scripts/brainbrowser/viewer/models/functional.mnc.raw",
      //    //  template: {
      //    //    element_id: "volume-ui-template",
      //    //    viewer_insert_class: "volume-viewer-display"
      //    //  }
      //    //}/*, function() {
      //    // $(".slice-display").css("display", "inline");
      //    // $(".volume-controls").css("width", "auto");
      //    // }*/);
      //  } else if ($(this).val() === "structural") {
      //    $("#sync-volumes-wrapper").show();
      //    viewer.clearVolumes();
      //    viewer.loadVolumes({
      //      volumes: [
      //        {
      //          type: "minc",
      //          header_url: "scripts/brainbrowser/viewer/models/structural4.mnc.header",
      //          raw_data_url: "scripts/brainbrowser/viewer/models/structural4.mnc.raw",
      //          template: {
      //            element_id: "volume-ui-template",
      //            viewer_insert_class: "volume-viewer-display"
      //          }
      //        },
      //        {
      //          type: 'minc',
      //          header_url: "scripts/brainbrowser/viewer/models/structural4.mnc.header",
      //          raw_data_url: "scripts/brainbrowser/viewer/models/structural4.mnc.raw",
      //          template: {
      //            element_id: "volume-ui-template",
      //            viewer_insert_class: "volume-viewer-display"
      //          }
      //        }
      //      ],
      //      overlay: {
      //        template: {
      //          element_id: "overlay-ui-template",
      //          viewer_insert_class: "overlay-viewer-display"
      //        }
      //      }
      //    });
      //  } else {
      //    $("#volume-file").show();
      //    viewer.clearVolumes();
      //  }
      //});

      // Display only the volume selected.
      // @TODO: add a 'on-click' function for the file explorer to display the right control panel if a volume is selected
      $("#volume-selection").change(function () {
        var volume_id = parseInt($(this).val());
        $("[id^=volume-panel-]").hide();
        $("#volume-panel-" + volume_id).show();
      });

      // Change viewer panel canvas size.
      //@TODO: check if the size is really updated and not just interpolated
      $("#panel-size").change(function () {
        var size = parseInt($(this).val(), 10);

        viewer.setPanelSize(size, size, {scale_image: true});
        viewer.redrawVolumes();
      });

      //Better than the selector for the size of the panel
      //This function resize dynamically the size of the panel when the window is resized
      $(window).resize(function () {
        var size = 0.75 * ($('.overlay-volume-controls').width()) / 3;
        size = size - 3.3;
        viewer.setPanelSize(size, size, {scale_image: true});
        viewer.redrawVolumes();
      });

      // Should cursors in all panels be synchronized?
      // @TODO: This functionality is useless, should be deleted
      $("#sync-volumes").change(function () {
        var synced = $(this).is(":checked");
        if (synced) {
          viewer.resetDisplays();
          viewer.redrawVolumes();
        }

        viewer.synced = synced;
      });

      // This will create an image of all the display panels
      // currently being shown in the viewer.
      $("#screenshot").click(function () {
        var width = 0;
        var height = 0;
        var active_panel = viewer.active_panel;

        // Create a canvas on which we'll draw the images.
        var canvas = document.createElement("canvas");
        var context = canvas.getContext("2d");
        var img = new Image();

        viewer.volumes.forEach(function (volume) {
          volume.display.forEach(function (panel) {
            width = Math.max(width, panel.canvas.width);
            height = Math.max(height, panel.canvas.height);
          });
        });

        canvas.width = width * viewer.volumes.length;
        canvas.height = height * 3;
        context.fillStyle = "#000000";
        context.fillRect(0, 0, canvas.width, canvas.height);

        // The active canvas is highlighted by the viewer,
        // so we set it to null and redraw the highlighting
        // isn't shown in the image.
        if (active_panel) {
          active_panel.updated = true;
          viewer.active_panel = null;
          viewer.draw();
        }

        viewer.volumes.forEach(function (volume, x) {
          volume.display.forEach(function (panel, axis_name, y) {
            context.drawImage(panel.canvas, x * width, y * height);
          });
        });

        // Restore the active canvas.
        if (active_panel) {
          active_panel.updated = true;
          viewer.active_panel = active_panel;
          viewer.draw();
        }

        // Show the created image in a dialog box.
        img.onload = function () {
          $("<div></div>").append(img).dialog({
            title: "Slices",
            height: img.height,
            width: img.width,
            show: {
              effect: "blind",
              duration: 1000
            }
          });
        };

        img.src = canvas.toDataURL();
      });


      //////////////////////////////////
      // Per volume UI hooks go in here.
      //////////////////////////////////
      viewer.addEventListener("volumeuiloaded", function (event) {
        var container = event.container;
        var volume = event.volume;
        var vol_id = event.volume_id;

        //Generate the volume selector to select the active panel
        //@TODO: Fix the list generation: Should be updated from scratch when a volume is loaded.
        //@TODO: AND we have to find a way to edit the BrainBrowser html code for each iteration (for the file browser)
        $("#volume-selection, #list_sortable").empty(); //flush the list
        for (var i = 0; i < vol_id; i++) {
          $("#volume-selection").append("<option value=" + (i) + ">Volume " + (i) + "</option>");
          //The file explorer - part1
          //generate the list of items
          //$("#list_sortable").append("<li><a id ='layer-" + (i) + "'><strong>Brain Volume_ID: </strong>" + (i) + "</a></li>");
          $("#list_sortable").append("<li><a id ='layer-" + (i) + "'><span class='glyphicon glyphicon-eye-open push-left'></span><strong> -  Brain Volume_ID: </strong>" + (i) + "</a></li>");

          if (($('#volume-selection').children().length > 1) && (i == vol_id - 1)) {
            //that hide element in the select to avoid overlapping volume controls
            $("[id^=volume-panel-]").hide();
            $("#volume-panel-" + 0).show();
          }


        }


        container = $(container);

        container.find(".button").button();

        // The world coordinate input fields.
        container.find(".world-coords").change(function () {
          var div = $(this);

          var x = parseFloat(div.find("#world-x-" + vol_id).val());
          var y = parseFloat(div.find("#world-y-" + vol_id).val());
          var z = parseFloat(div.find("#world-z-" + vol_id).val());

          // Make sure the values are numeric.
          if (!BrainBrowser.utils.isNumeric(x)) {
            x = 0;
          }
          if (!BrainBrowser.utils.isNumeric(y)) {
            y = 0;
          }
          if (!BrainBrowser.utils.isNumeric(z)) {
            z = 0;
          }

          // Set coordinates and redraw.
          viewer.volumes[vol_id].setWorldCoords(x, y, z);

          viewer.redrawVolumes();
        });

        // The world coordinate input fields.
        container.find(".voxel-coords").change(function () {
          var div = $(this);

          var i = parseInt(div.find("#voxel-i-" + vol_id).val(), 10);
          var j = parseInt(div.find("#voxel-j-" + vol_id).val(), 10);
          var k = parseInt(div.find("#voxel-k-" + vol_id).val(), 10);

          // Make sure the values are numeric.
          if (!BrainBrowser.utils.isNumeric(i)) {
            i = 0;
          }
          if (!BrainBrowser.utils.isNumeric(j)) {
            j = 0;
          }
          if (!BrainBrowser.utils.isNumeric(k)) {
            k = 0;
          }

          // Set coordinates and redraw.
          viewer.volumes[vol_id].setVoxelCoords(i, j, k);

          viewer.redrawVolumes();
        });

        // Color map URLs are read from the config file and added to the
        // color map select box.
        var color_map_select = $('<select id="color-map-select"></select>').change(function () {
          var selection = $(this).find(":selected");

          viewer.loadVolumeColorMapFromURL(vol_id, selection.val(), selection.data("cursor-color"), function () {
            viewer.redrawVolumes();
          });
        });

        BrainBrowser.config.get("color_maps").forEach(function (color_map) {
          color_map_select.append('<option value="' + color_map.url +
            '" data-cursor-color="' + color_map.cursor_color + '">' +
            color_map.name + '</option>'
          );

        });

        $("#color-map-" + vol_id).append(color_map_select);

        // Load a color map select by the user.
        container.find(".color-map-file").change(function () {
          viewer.loadVolumeColorMapFromFile(vol_id, this, "#FF0000", function () {
            viewer.redrawVolumes();
          });
        });

        // Change the range of intensities that will be displayed.
        container.find(".threshold-div").each(function () {
          var div = $(this);

          // Input fields to input min and max thresholds directly.
          var min_input = div.find("#min-threshold-" + vol_id);
          var max_input = div.find("#max-threshold-" + vol_id);

          // Slider to modify min and max thresholds.
          var slider = div.find(".slider");

          slider.slider({
            range: true,
            min: 0,
            max: 255,
            values: [0, 255],
            step: 1,
            slide: function (event, ui) {
              var values = ui.values;

              // Update the input fields.
              min_input.val(values[0]);
              max_input.val(values[1]);

              // Update the volume and redraw.
              volume.intensity_min = values[0];
              volume.intensity_max = values[1];
              viewer.redrawVolumes();
            },
            stop: function () {
              $(this).find("a").blur();
            }
          });

          // Input field for minimum threshold.
          min_input.change(function () {
            var value = parseFloat(this.value);

            // Make sure input is numeric and in range.
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 0;
            }
            value = Math.max(0, Math.min(value, 255));
            this.value = value;

            // Update the slider.
            slider.slider("values", 0, value);

            // Update the volume and redraw.
            volume.intensity_min = value;
            viewer.redrawVolumes();
          });

          max_input.change(function () {
            var value = parseFloat(this.value);

            // Make sure input is numeric and in range.
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 255;
            }
            value = Math.max(0, Math.min(value, 255));
            this.value = value;

            // Update the slider.
            slider.slider("values", 1, value);

            // Update the volume and redraw.
            volume.intensity_max = value;
            viewer.redrawVolumes();
          });

        });

        container.find(".time-div").each(function () {
          var div = $(this);

          if (volume.header.time) {
            div.show();
          } else {
            return;
          }

          var slider = div.find(".slider");
          var time_input = div.find("#time-val-" + vol_id);
          var play_button = div.find("#play-" + vol_id);

          var min = 0;
          var max = volume.header.time.space_length - 1;
          var play_interval;

          slider.slider({
            min: min,
            max: max,
            value: 0,
            step: 1,
            slide: function (event, ui) {
              var value = +ui.value;
              time_input.val(value);
              volume.current_time = value;
              viewer.redrawVolumes();
            },
            stop: function () {
              $(this).find("a").blur();
            }
          });

          time_input.change(function () {
            var value = parseInt(this.value, 10);
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 0;
            }

            value = Math.max(min, Math.min(value, max));

            this.value = value;
            time_input.val(value);
            slider.slider("value", value);
            volume.current_time = value;
            viewer.redrawVolumes();
          });

          play_button.change(function () {
            if (play_button.is(":checked")) {
            } else {
            }
          });

        });

        // Create an image of all slices in a certain
        // orientation.
        container.find(".slice-series-div").each(function () {
          var div = $(this);

          var space_names = {
            xspace: "Sagittal",
            yspace: "Coronal",
            zspace: "Transverse"
          };

          div.find(".slice-series-button").click(function () {
            var axis_name = $(this).data("axis");
            var axis = volume.header[axis_name];
            var space_length = axis.space_length;
            var time = volume.current_time;
            var per_column = 10;
            var zoom = 0.5;
            var i, x, y;

            // Canvas on which to draw the images.
            var canvas = document.createElement("canvas");
            var context = canvas.getContext("2d");

            // Get first slice to set dimensions of the canvas.
            var image_data = volume.getSliceImage(volume.slice(axis_name, 0, time), zoom);
            var img = new Image();
            canvas.width = per_column * image_data.width;
            canvas.height = Math.ceil(space_length / per_column) * image_data.height;
            context.fillStyle = "#000000";
            context.fillRect(0, 0, canvas.width, canvas.height);

            // Draw the slice on the canvas.
            context.putImageData(image_data, 0, 0);

            // Draw the rest of the slices on the canvas.
            for (i = 1; i < space_length; i++) {
              image_data = volume.getSliceImage(volume.slice(axis_name, i, time), zoom);
              x = i % per_column * image_data.width;
              y = Math.floor(i / per_column) * image_data.height;
              context.putImageData(image_data, x, y);
            }

            // Retrieve image from canvas and display it
            // in a dialog box.
            img.onload = function () {
              $("<div></div>").append(img).dialog({
                title: space_names[axis_name] + " Slices",
                height: 600,
                width: img.width
              });
            };

            img.src = canvas.toDataURL();
          });
        });


        // Blend controls for a multivolume overlay.
        container.find(".blend-div").each(function () {
          var div = $(this);
          var slider = div.find(".slider");
          var blend_input_min = div.find("#blend-val-min");
          var blend_input_max = div.find("#blend-val-max");
          var images_order = (function (a, b) {
            while (a--)b[a] = a;
            return b
          })(viewer.volumes.length - 1, []);
          var to_hide = [];


          //The file explorer - part2
          $("#list_sortable")
            .sortable({
              start: function (event, ui) {
                ui.item.startPos = ui.item.index();
              },
              //move a slide when it's drag and drop into the list
              update: function (event, ui) {
                //alert("New position: " + ui.item.index() + " last position: " + ui.item.startPos);
                images_order.splice(ui.item.index(), 0, images_order.splice(ui.item.startPos, 1)[0]);
                volume.images_order = images_order;
                volume.display.refreshPanels();
                viewer.redrawVolumes();
              }
            });
          //Hide elements of the list on double click
          $("#list_sortable a").dblclick(function (event, ui) {
            var volid = parseInt($(this).attr('id').split('-')[1]);
            //to add one element in the array
            if (!($.inArray(volid, to_hide) > -1)) {
              to_hide.push(volid);
              $(this).css("text-decoration", "line-through");
              $(this).children('span').toggleClass("glyphicon-eye-open glyphicon-eye-close");
            }
            else {
              //to delete one element of the array
              to_hide = jQuery.grep(to_hide, function (value) {
                return value != volid;
              });
              $(this).css("text-decoration", "none");
              $(this).children('span').toggleClass("glyphicon-eye-close glyphicon-eye-open");
            }

            volume.to_hide = to_hide;
            volume.display.refreshPanels();
            viewer.redrawVolumes();
          });
          $("#list_sortable a").click(function () {
            layer_id = parseInt($(this).attr('id').split('-')[1]);
            $("[id^=volume-panel-]").hide();
            $("#volume-panel-" + layer_id).show();
            $("#list_sortable a").removeClass('onclick');
            $(this).addClass('onclick');
          });
          //This function delete a volume when dropped on the trash
          //This is a real deletion inside the volume list, if you need to hide the volume, just double click on it!
          $(".trash").droppable({
            hoverClass: "trash-hover",
            tolerance: "touch",
            drop: function (event, ui) {
              //get the volume id of the dragged element (this information is inside the id attribute)
              var vol_selected = $(ui.draggable).children().attr('id').split('-')[1];
              //Splice is use to delete an element in an array
              volumes_files.splice(vol_selected, 1);
              //Clear every volume in order to redraw everything
              viewer.clearVolumes();
              //remove the item in the list (this is just a security, because the loadVolume() will do it)
              ui.draggable.remove();
              viewer.loadVolumes(load_params);

            }
          });


          //Simulate click on the hidden file input
          $('.add-volume').click(function (event) {
            $('#header-file').click();
          });
          // Load a new model from a file that the user has
          // selected.
          //@TODO: add a filetype detection to load minc OR nifti
          //@TODO: Fix that to support gziped files
          $("#header-file").change(function () {
            console.log('hello')

            var new_volume_to_add = {
              type: "nifti1",
              nii_file: document.getElementById("header-file"),
              template: {
                element_id: "volume-ui-template",
                viewer_insert_class: "volume-viewer-display"
              }
            };

            volumes_files.push(new_volume_to_add);
            viewer.clearVolumes();

            viewer.loadVolumes(load_params);
          });

          // Slider to select blend value.
          slider.slider({
            range: true,
            min: 0,
            max: 255,
            step: 0.01,
            values: [0, 100],
            slide: function (event, ui) {
              var values = ui.values;
              volume.blend_ratios[0] = values[0];
              volume.blend_ratios[1] = values[1];

              blend_input_min.val(values[0]);
              blend_input_max.val(values[1]);
              viewer.redrawVolumes();
            },
            stop: function () {
              $(this).find("a").blur();
            }
          });


          // Input field to select blend values explicitly.
          blend_input_min.change(function () {
            var value = parseFloat(this.value);

            // Check that input is numeric and in range.
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 0;
            }
            value = Math.max(0, Math.min(value, 255));
            this.value = value;

            // Update slider and redraw volumes.
            slider.slider("values", 0, value);
            volume.blend_ratios[0] = value[0];
            viewer.redrawVolumes();
          });

          blend_input_max.change(function () {
            var value = parseFloat(this.value);

            // Check that input is numeric and in range.
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 0;
            }
            value = Math.max(0, Math.min(value, 255));
            this.value = value;

            // Update slider and redraw volumes.
            slider.slider("values", 1, value);
            volume.blend_ratios[1] = value[1];
            viewer.redrawVolumes();
          });
        });


        // Contrast controls
        container.find(".contrast-div").each(function () {
          var div = $(this);
          var slider = div.find(".slider");
          var contrast_input = div.find("#contrast-val");

          // Slider to select contrast value.
          slider.slider({
            min: 0,
            max: 2,
            step: 0.05,
            value: 1,
            slide: function (event, ui) {
              var value = parseFloat(ui.value);
              volume.display.setContrast(value);
              volume.display.refreshPanels();

              contrast_input.val(value);
            },
            stop: function () {
              $(this).find("a").blur();
            }
          });

          // Input field to select contrast values explicitly.
          contrast_input.change(function () {
            var value = parseFloat(this.value);

            // Check that input is numeric and in range.
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 0;
            }
            value = Math.max(0, Math.min(value, 2));
            this.value = value;

            // Update slider and redraw volumes.
            slider.slider("value", value);
            volume.display.setContrast(value);
            volume.display.refreshPanels();
            viewer.redrawVolumes();
          });
        });

        // Contrast controls
        container.find(".brightness-div").each(function () {
          var div = $(this);
          var slider = div.find(".slider");
          var brightness_input = div.find("#brightness-val");

          // Slider to select brightness value.
          slider.slider({
            min: -1,
            max: 1,
            step: 0.05,
            value: 0,
            slide: function (event, ui) {
              var value = parseFloat(ui.value);
              volume.display.setBrightness(value);
              volume.display.refreshPanels();

              brightness_input.val(value);
            },
            stop: function () {
              $(this).find("a").blur();
            }
          });

          // Input field to select brightness values explicitly.
          brightness_input.change(function () {
            var value = parseFloat(this.value);

            // Check that input is numeric and in range.
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 0;
            }
            value = Math.max(-1, Math.min(value, 1));
            this.value = value;

            // Update slider and redraw volumes.
            slider.slider("value", value);
            volume.display.setBrightness(value);
            volume.display.refreshPanels();
            viewer.redrawVolumes();
          });
        });

        // Transparency controls
        container.find(".alpha-div").each(function () {
          var div = $(this);
          var slider = div.find(".slider");
          var alpha_input = div.find("#alpha-val");

          // Slider to select alpha value.
          slider.slider({
            min: 0,
            max: 1,
            step: 0.01,
            value: 1,
            slide: function (event, ui) {
              var value = parseFloat(ui.value);
              volume.setAlphaValue(1, 1, value);
              volume.display.refreshPanels();

              alpha_input.val(value);
            },
            stop: function () {
              $(this).find("a").blur();
            }
          });

          // Input field to select alpha values explicitly.
          alpha_input.change(function () {
            var value = parseFloat(this.value);

            // Check that input is numeric and in range.
            if (!BrainBrowser.utils.isNumeric(value)) {
              value = 0;
            }
            value = Math.max(0, Math.min(value, 1));
            this.value = value;

            // Update slider and redraw volumes.
            slider.slider("value", value);
            volume.setAlphaValue(1, 1, value);
            viewer.redrawVolumes();
          });
        });
      });

      /////////////////////////////////////////////////////
      // UI updates to be performed after each slice update.
      //////////////////////////////////////////////////////
      viewer.addEventListener("sliceupdate", function (event) {
        var panel = event.target;
        var volume = event.volume;
        var vol_id = panel.volume_id;
        var world_coords, voxel_coords;
        var value;

        if (BrainBrowser.utils.isFunction(volume.getWorldCoords)) {
          world_coords = volume.getWorldCoords();
          $("#world-x-" + vol_id).val(world_coords.x.toPrecision(3));
          $("#world-y-" + vol_id).val(world_coords.y.toPrecision(3));
          $("#world-z-" + vol_id).val(world_coords.z.toPrecision(3));
        }

        if (BrainBrowser.utils.isFunction(volume.getVoxelCoords)) {
          voxel_coords = volume.getVoxelCoords();
          $("#voxel-i-" + vol_id).val(parseInt(voxel_coords.i, 10));
          $("#voxel-j-" + vol_id).val(parseInt(voxel_coords.j, 10));
          $("#voxel-k-" + vol_id).val(parseInt(voxel_coords.k, 10));
        }

        value = volume.getIntensityValue();
        $("#intensity-value-" + vol_id)
          .css("background-color", "#" + volume.color_map.colorFromValue(value, {
            hex: true,
            min: volume.min,
            max: volume.max,
            contrast: panel.contrast,
            brightness: panel.brightness
          }))
          .html(Math.floor(value));

        if (volume.header && volume.header.time) {
          $("#time-slider-" + vol_id).slider("option", "value", volume.current_time);
          $("#time-val-" + vol_id).val(volume.current_time);
        }
      });

      var color_map_config = BrainBrowser.config.get("color_maps")[0];

      loading_div.show();

      //////////////////////////////
      // Load the default color map.
      //////////////////////////////
      viewer.loadDefaultColorMapFromURL(BrainBrowser.config.get("color_maps")[2].url, color_map_config.cursor_color);
      ////////////////////////////////////////
      // Set the size of slice display panels.
      ////////////////////////////////////////
      viewer.setDefaultPanelSize(256, 256);

      ///////////////////
      // Start rendering.
      ///////////////////
      viewer.render();

      /////////////////////
      // Load the volumes.
      /////////////////////
      viewer.loadVolumes(load_params);

    });

  });
