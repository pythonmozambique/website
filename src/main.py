from browser import document
import navbar
import home
import aboutus
import events
import resources
import contacts
import footer

sections = [home, aboutus, events, resources, contacts, footer]

document <= navbar.create()

for sec in sections:
    document <= sec.create()
    sec.bind(document)