{
    'name': 'Odoo WhatsApp Integration | WhatsApp Cloud API | Odoo V18 Community Edition',
    'version': '18.1',
    'author': 'TechUltra Solutions Private Limited',
    'company': 'TechUltra Solutions Private Limited',
    'category': 'Base',
    'live_test_url': 'https://youtube.com/playlist?list=PL8o8i9mlxsWiGhybME4miEeftUCcTLNoj&si=FTo3Tmf1sE1NHr9h',
    'website': 'www.techultrasolutions.com',
    'price': 109,
    'currency': 'USD',
    'summary': """Meta Whatsapp chat all in one integrated with the sale purchase accounting discuss modules. all in one whatsapp can help you to take the advantage of the whatsapp communication in current market
        Odoo WhatsApp Integration
        WhatsApp Integration
        Odoo Meta WhatsApp Graph API
        Odoo V18 Community Edition
        Odoo V18 Community WhatsApp Integration
        V18 Community WhatsApp
        Omnichannel
        Meta
        Community WhatsApp
        Community
        WhatsApp Community
        Odoo WhatsApp Community
        Odoo WhatsApp Cloud API
        WhatsApp Cloud API
        WhatsApp Community Edition
    """,
    'description': """
        The WhatsApp Business Platform Cloud API is based on Meta/Facebook's Graph API Which allows medium and large businesses to communicate with their customers at scale. Send and receive whatsapp messages quickly & easily directly from Odoo to WhatsApp and WhatsApp to Odoo.
        Also, this module which allows the user to Create/Edit/Remove/Delete WhatsApp Templates, 
        Showing WhatsApp Chat History, Configure WhatsApp Templates in Particular User via Odoo.
        Odoo WhatsApp Integration
        WhatsApp Integration
        Odoo Meta WhatsApp Graph API
        Omnichannel
        Odoo V18 Community Edition
        Odoo V18 Community WhatsApp Integration
        V18 Community WhatsApp
        Community WhatsApp
        Meta
        Community
        WhatsApp Community
        Odoo WhatsApp Community
        Odoo WhatsApp Cloud API
        WhatsApp Cloud API
        WhatsApp Community Edition
    """,
    'depends': ['base', 'mail', 'mail_group', 'base_automation'],
    'data': [
        'security/whatsapp_security.xml',
        'security/ir.model.access.csv',
        'data/cron.xml',
        'data/wa_template.xml',
        'wizard/wa_compose_message_view.xml',
        'views/res_config_settings_views.xml',
        'views/provider_base.xml',
        'views/res_users.xml',
        'views/channel_provider_line.xml',
        'views/res_partner.xml',
        'views/whatsapp_history.xml',
        'views/wa_template.xml',
        'views/variables.xml',
        'views/components.xml',
        'views/mail_channel.xml',
        'views/mail_message.xml',
        'views/provider_meta.xml',
        'views/ir_actions.xml',
        'views/interactive_list_views.xml',
        'views/interactive_product_list_views.xml',
        'views/wa_button_component_views.xml',
        'views/wa_carousel_component_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/tus_meta_whatsapp_base/static/src/scss/kanban_view.scss',
            '/tus_meta_whatsapp_base/static/src/css/style.css',
        ],
    },
    'external_dependencies': {
        'python': ['phonenumbers'],
    },
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
    'images': ['static/description/tus_banner.gif'],
}
