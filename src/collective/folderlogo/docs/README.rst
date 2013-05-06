=====================
collective.folderlogo
=====================

collective.folderlogo changes logo images and their background under plone site or folders easily through the web.

Currently tested with
---------------------

* Plone-4.3 [taito]

* For older versions and python-2.6, use version 0.4.1.

How To
------

After installing through **Site Setup** --> **Addons**,
add Image with ID ``logo`` under plone site or whatever folder you want to change logos.

Changing ID of images
---------------------

1. Go to **Configuration registry** page from **Site Setup**.
2. Update **Log ID**, **Background Color** and **Background Image ID** from here.

**Background Color**
    Needs to be available for CSS styling background-color like: ``transparent``, ``#ffffff``.
