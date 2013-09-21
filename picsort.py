#! /usr/bin/env python2

import os
import gtk
import gtk.gdk
import gobject

import json

MAX_IMG_WIDTH = 800.0
MAX_IMG_HEIGHT = 800.0

interface = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <requires lib="gtk+" version="2.24"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkImage" id="addSymbol">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-add</property>
  </object>
  <object class="GtkImage" id="clearSymbol">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-clear</property>
  </object>
  <object class="GtkFileChooserDialog" id="fileLoader">
    <property name="can_focus">False</property>
    <property name="border_width">5</property>
    <property name="title" translatable="yes">Load...</property>
    <property name="role">GtkFileChooserDialog</property>
    <property name="type_hint">dialog</property>
    <property name="action">save</property>
    <property name="local_only">False</property>
    <property name="show_hidden">True</property>
    <child internal-child="vbox">
      <object class="GtkVBox" id="dialog-vbox7">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkHButtonBox" id="dialog-action_area7">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="layout_style">end</property>
            <child>
              <object class="GtkButton" id="button5">
                <property name="label">gtk-cancel</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="button6">
                <property name="label">gtk-open</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="pack_type">end</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <placeholder/>
        </child>
      </object>
    </child>
    <action-widgets>
      <action-widget response="-1">button5</action-widget>
      <action-widget response="0">button6</action-widget>
    </action-widgets>
  </object>
  <object class="GtkFileChooserDialog" id="fileSaver">
    <property name="can_focus">False</property>
    <property name="border_width">5</property>
    <property name="title" translatable="yes">Save as...</property>
    <property name="role">GtkFileChooserDialog</property>
    <property name="type_hint">dialog</property>
    <property name="action">save</property>
    <property name="local_only">False</property>
    <child internal-child="vbox">
      <object class="GtkVBox" id="dialog-vbox3">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkHButtonBox" id="dialog-action_area3">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="layout_style">end</property>
            <child>
              <object class="GtkButton" id="button3">
                <property name="label">gtk-cancel</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="button4">
                <property name="label">gtk-save</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="pack_type">end</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <placeholder/>
        </child>
      </object>
    </child>
    <action-widgets>
      <action-widget response="-1">button3</action-widget>
      <action-widget response="0">button4</action-widget>
    </action-widgets>
  </object>
  <object class="GtkFileChooserDialog" id="folderChooser">
    <property name="can_focus">False</property>
    <property name="border_width">5</property>
    <property name="role">GtkFileChooserDialog</property>
    <property name="modal">True</property>
    <property name="destroy_with_parent">True</property>
    <property name="type_hint">dialog</property>
    <property name="action">select-folder</property>
    <child internal-child="vbox">
      <object class="GtkVBox" id="dialog-vbox1">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkHButtonBox" id="dialog-action_area1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="layout_style">end</property>
            <child>
              <object class="GtkButton" id="button2">
                <property name="label">gtk-cancel</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="button1">
                <property name="label">gtk-open</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="pack_type">end</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <placeholder/>
        </child>
      </object>
    </child>
    <action-widgets>
      <action-widget response="-1">button2</action-widget>
      <action-widget response="0">button1</action-widget>
    </action-widgets>
  </object>
  <object class="GtkImage" id="image3">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-open</property>
  </object>
  <object class="GtkImage" id="nextSymbol">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-media-next</property>
  </object>
  <object class="GtkImage" id="openSymbol">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-open</property>
  </object>
  <object class="GtkImage" id="prevSymbol">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-media-previous</property>
  </object>
  <object class="GtkWindow" id="window">
    <property name="can_focus">False</property>
    <signal name="delete-event" handler="onQuit" swapped="no"/>
    <child>
      <object class="GtkVBox" id="vbox1">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <child>
          <object class="GtkMenuBar" id="menubar1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkMenuItem" id="fileMenuItem">
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_File</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="chooseFolder">
                        <property name="label" translatable="yes">Choose source folder</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="image">image3</property>
                        <property name="use_stock">False</property>
                        <signal name="activate" handler="onChooseFolder" swapped="no"/>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="clearCategories">
                        <property name="label" translatable="yes">Clear categories</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="image">clearSymbol</property>
                        <property name="use_stock">False</property>
                        <signal name="activate" handler="onClearCategories" swapped="no"/>
                      </object>
                    </child>
                    <child>
                      <object class="GtkSeparatorMenuItem" id="separatormenuitem">
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="loadConfig">
                        <property name="label" translatable="yes">Load config</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="image">openSymbol</property>
                        <property name="use_stock">False</property>
                        <accelerator key="o" signal="activate" modifiers="GDK_CONTROL_MASK"/>
                        <signal name="activate" handler="onLoadConfig" swapped="no"/>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="saveConfig">
                        <property name="label">gtk-save</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <accelerator key="s" signal="activate" modifiers="GDK_CONTROL_MASK"/>
                        <signal name="activate" handler="onSaveConfig" swapped="no"/>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="saveConfigAs">
                        <property name="label">gtk-save-as</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <accelerator key="s" signal="activate" modifiers="GDK_SHIFT_MASK | GDK_CONTROL_MASK"/>
                        <signal name="activate" handler="onSaveConfigAs" swapped="no"/>
                      </object>
                    </child>
                    <child>
                      <object class="GtkSeparatorMenuItem" id="separatormenuitem1">
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="quit">
                        <property name="label">gtk-quit</property>
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <accelerator key="w" signal="activate" modifiers="GDK_CONTROL_MASK"/>
                        <signal name="activate" handler="onQuit" swapped="no"/>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkHBox" id="hbox3">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkVBox" id="CategoryRows">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkHBox" id="categoryRow1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkHBox" id="categoryRow2">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="newCategoryButton">
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="image">addSymbol</property>
                <property name="image_position">right</property>
                <signal name="clicked" handler="onAddCategory" swapped="no"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkVBox" id="vbox2">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkHBox" id="hbox2">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkVBox" id="vbox4">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkButton" id="prevButton">
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="image">prevSymbol</property>
                        <accelerator key="comma" signal="clicked"/>
                        <signal name="clicked" handler="onPrevImage" swapped="no"/>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">False</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkImage" id="imagePreview">
                    <property name="width_request">400</property>
                    <property name="height_request">400</property>
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="stock">gtk-missing-image</property>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkVBox" id="vbox3">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkButton" id="nextButton">
                        <property name="use_action_appearance">False</property>
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="receives_default">True</property>
                        <property name="image">nextSymbol</property>
                        <accelerator key="period" signal="clicked"/>
                        <signal name="clicked" handler="onNextImage" swapped="no"/>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">False</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">2</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="infoLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkHBox" id="hbox1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkEntry" id="renameField">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="invisible_char">•</property>
                <property name="primary_icon_activatable">False</property>
                <property name="secondary_icon_activatable">False</property>
                <property name="primary_icon_sensitive">True</property>
                <property name="secondary_icon_sensitive">True</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="renameButton">
                <property name="label" translatable="yes">Rename</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <accelerator key="r" signal="clicked" modifiers="GDK_CONTROL_MASK"/>
                <signal name="clicked" handler="onRename" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">3</property>
          </packing>
        </child>
        <child>
          <object class="GtkHBox" id="hbox4">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkButton" id="deleteButton">
                <property name="label" translatable="yes">Delete</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <accelerator key="Delete" signal="clicked"/>
                <signal name="clicked" handler="onDelete" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="undoButton">
                <property name="label" translatable="yes">Undo</property>
                <property name="use_action_appearance">False</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <accelerator key="z" signal="clicked" modifiers="GDK_CONTROL_MASK"/>
                <signal name="clicked" handler="onUndo" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">4</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""

def scaleImage(pixbuf, width, height):
    width_ratio = float(width) / pixbuf.get_width()
    height_ratio = float(height) / pixbuf.get_height()
    min_ratio = min(width_ratio, height_ratio, 1)
    pixbuf = pixbuf.scale_simple(
            int(pixbuf.get_width() * min_ratio),
            int(pixbuf.get_height() * min_ratio),
            gtk.gdk.INTERP_BILINEAR
            )
    return pixbuf

class CategoryButton(gtk.Button):
    def __init__(self, owner, categoryNumber):
        gtk.Button.__init__(self)
        self.handler_id = self.connect("clicked", owner.onCategoryChosen, categoryNumber)

class PicSort:

    def onLoadConfig(self, widget, data=None):
        loadDialog = self.widgets["fileLoader"]
        response = loadDialog.run()
        if response == 0 :
            self.loadConfig(loadDialog.get_filename())
            gtk.recent_manager_get_default().add_item(loadDialog.get_uri())
        loadDialog.hide()

    def loadConfig(self, configFile):
        with open(configFile, "r") as inFile:
            data = json.load(inFile)

            self.clearCategories()
            for cat in data["categories"]:
                self.addNewCategory(cat)

            self.setFolder(data["source"])
            self.configFile = configFile

    def onSaveConfig(self, widget, data=None):
        if len(self.configFile) == 0 :
            self.onSaveConfigAs(widget, data)
        else:
            self.saveConfig(self.configFile)

    def onSaveConfigAs(self, widget, data=None):
        saveDialog = self.widgets["fileSaver"]
        response = saveDialog.run()
        if(response == 0):
            self.saveConfig(saveDialog.get_filename())
        saveDialog.hide()

    def saveConfig(self, configFile):
        data = {"source" : self.sourceFolder,
                "categories" : self.categories}
        with open(configFile, "w") as outFile:
            json.dump(data, outFile)
            self.configFile = configFile

    def onQuit(self, widget, data=None):
        gtk.main_quit()

    def onChooseFolder(self, widget, data=None):
        folderChooser = self.widgets["folderChooser"]
        folderChooser.set_title("Choose a source folder...")
        response = folderChooser.run()
        if response == 0 :
            self.setFolder(folderChooser.get_filename())

        folderChooser.hide()

    def setFolder(self, folder):
        self.sourceFolder = folder
        self.imageFiles = [
                os.path.join(self.sourceFolder, path) for path in os.listdir(self.sourceFolder)
                ]
        self.currentImageIndex = 0

        self.showImage()

    def onAddCategory(self, widget, data=None):
        #Get category folder
        folderChooser = self.widgets["folderChooser"]
        folderChooser.set_title("Choose a destination folder...")
        response = folderChooser.run()

        if response != 0 :
            folderChooser.hide()
            return

        folderName = folderChooser.get_filename()
        folderPath = folderChooser.get_current_folder()
        folderChooser.hide()

        self.addNewCategory(folderName)

    def addNewCategory(self, folderName):
        catNumber = len(self.categories)
        self.categories.append(os.path.join(folderName))

        categoryButton = CategoryButton(self, catNumber)
        categoryButton.set_label("{0}. {1}".format(catNumber+1, os.path.basename(folderName)))

        self.placeButton(categoryButton, catNumber)

    def onClearCategories(self, widget, data=None):
        self.clearCategories()

    def clearCategories(self):
        self.categories = []
        row = self.widgets["categoryRow1"]
        for button in row.get_children() :
            row.remove(button)
            button.destroy()
        row = self.widgets["categoryRow2"]
        for button in row.get_children() :
            row.remove(button)
            button.destroy()

    def placeButton(self, button, number):
        buttonRow = None
        if number >= 5 :
            buttonRow = self.widgets["categoryRow2"]
            number -= 5
        else :
            buttonRow = self.widgets["categoryRow1"]
        buttonRow.pack_start(button)
        buttonRow.reorder_child(button, number)
        buttonRow.show_all()

    def onShortcutPressed(self, widget, event):
        keyPressed = event.string
        if (len(keyPressed) != 1) or (not keyPressed.isalnum()):
            return

        catNum = int(keyPressed) - 1
        if catNum < len(self.imageFiles) :
            self.onCategoryChosen(widget, catNum)

    def onCategoryChosen(self, widget, data):
        oldName = self.imageFiles[self.currentImageIndex]
        newName = os.path.join(self.categories[data], os.path.basename(oldName))
        os.rename(oldName, newName)
        del self.imageFiles[self.currentImageIndex]
        self.lastMove = (oldName, newName)
        self.showImage()

    def onRename(self, widget, data=None):
        oldName = self.imageFiles[self.currentImageIndex]
        newName = os.path.join(self.sourceFolder, self.widgets["renameField"].get_text())
        os.rename(oldName, newName)
        self.imageFiles[self.currentImageIndex] = newName
        self.showImage()

    def onNextImage(self, widget, data=None):
        self.currentImageIndex += 1
        self.showImage()

    def onPrevImage(self, widget, data=None):
        self.currentImageIndex -= 1
        self.currentImageIndex %= len(self.imageFiles)
        self.showImage()

    def showImage(self):
        pixBuf = None
        imageFile = ""

        while True:
            try:
                if self.currentImageIndex >= len(self.imageFiles):
                    self.currentImageIndex = 0
                if len(self.imageFiles) == 0:
                    self.widgets["imagePreview"].clear()
                    self.widgets["infoLabel"].set_text("No image files in {0}".format(self.sourceFolder))
                    return

                imageFile = self.imageFiles[self.currentImageIndex]
                pixBuf = gtk.gdk.pixbuf_new_from_file(imageFile)
                break
            except gobject.GError:
                del self.imageFiles[self.currentImageIndex]

        actualSize = self.widgets["imagePreview"].get_allocation()
        pixBuf = scaleImage(pixBuf, actualSize.width, actualSize.height)
        self.widgets["imagePreview"].set_from_pixbuf(pixBuf)
        self.widgets["infoLabel"].set_text( "{0} {1}/{2}".format(
            imageFile, self.currentImageIndex+1, len(self.imageFiles)
            ))

        self.widgets["renameField"].set_text(os.path.basename(imageFile))

    def onImageResize(self, widget, data=None):
        self.showImage()

    def saveWidgets(self, builder):
        self.widgets = {}

        for widget in builder.get_objects():
            self.widgets[gtk.Buildable.get_name(widget)] = widget

    def onUndo(self, widget, data=None):
        if self.lastMove:
            os.rename(self.lastMove[1], self.lastMove[0])
            self.imageFiles.insert(self.currentImageIndex, self.lastMove[0])
            self.lastMove = None
            self.showImage()

    def onDelete(self, widget, data=None):
        os.remove(self.imageFiles[self.currentImageIndex])
        del self.imageFiles[self.currentImageIndex]
        self.showImage()


    def __init__(self):
        builder = gtk.Builder()
        #builder.add_from_file("picsort.glade")
        builder.add_from_string(interface)
        self.window = builder.get_object("window")
        builder.connect_signals(self)

        self.saveWidgets(builder)
        self.setFolder(os.getcwd())
        self.categories = []
        self.configFile = ""
        self.window.connect_after("key-press-event", self.onShortcutPressed)
        self.lastMove = None

if __name__ == "__main__":
    mainWindow = PicSort()
    mainWindow.window.show()
    gtk.main()
