import bpy

addon_keymaps = []

def register():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = "Node Editor", space_type = "NODE_EDITOR")

    # Open the ctrl-A search menu
    kmi = km.keymap_items.new("an.node_search", type = "A", value = "PRESS", ctrl = True)

    # Open the context sensitive pie menu
    kmi = km.keymap_items.new("wm.call_menu_pie", type = "W", value = "PRESS")
    kmi.properties.name = "an.context_pie"

    # Just temporary
    kmi = km.keymap_items.new("an.make_group_template_operator", type = "U", value = "PRESS")

    addon_keymaps.append(km)

def unregister():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()
