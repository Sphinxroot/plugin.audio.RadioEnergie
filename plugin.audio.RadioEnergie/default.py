########################################

import os, sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon
	
#Radio Energie en Direct By Sphinxroot QC

# Various constants used throughout the script
HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon(id='plugin.audio.RadioEnergie')
LANGUAGE  = ADDON.getLocalizedString
THUMBNAIL_PATH = os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media')

def start() :

	li = xbmcgui.ListItem(label=LANGUAGE(30000), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Drummondville.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://20263.live.streamtheworld.com/CJDMFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30001), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Gatineau.png'))		
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://20263.live.streamtheworld.com/CKTFFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30002), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Estrie.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://22113.live.streamtheworld.com/CIMOFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30003), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Montreal.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://16613.live.streamtheworld.com/CKMFFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30004), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Quebec.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://18123.live.streamtheworld.com/CHIKFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30005), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Est.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://15903.live.streamtheworld.com/CIKIFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30006), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Abitibi-99.1.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://18133.live.streamtheworld.com/CJMMFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30007), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-saguenay.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://20263.live.streamtheworld.com/CJABFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30008), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Mauricie.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://17443.live.streamtheworld.com/CIGBFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30009), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Energie-Abitibi.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://20263.live.streamtheworld.com/CJMVFMAAC.aac", listitem=li, isFolder=False)
	setViewMode("500")		
	xbmcplugin.endOfDirectory( HANDLE )		
	
def setViewMode(id):
	if xbmc.getSkinDir() == "skin.confluence":
		xbmc.executebuiltin("Container.SetViewMode(" + id + ")")
			
start()