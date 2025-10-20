{
    "name": "Portal Fix - Remove Duplicate Composer",
    "version": "1.1",
    "author": "Hotfix",
    "depends": ["portal"],
    "assets": {
        "web.assets_frontend": [
            ("remove", "portal/static/src/js/portal_composer.js"),
        ],
        "portal.assets_chatter": [
            # Quitamos cualquier archivo que vuelva a meter el Composer
            ("remove", "mail/static/src/model/**/*"),
            ("remove", "portal/static/src/chatter/core/**/*"),
            ("remove", "portal/static/src/chatter/frontend/**/*"),
        ],
    },
    "installable": True,
    "auto_install": False,
}
