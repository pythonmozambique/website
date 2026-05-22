from browser import document
import navbar
import hero
import aboutus
import events
import resources
import contacts
import footer

sections = [hero, aboutus, events, resources, contacts, footer]

document <= navbar.create()

for sec in sections:
    document <= sec.create()
    sec.bind(document)