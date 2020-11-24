# Copyright (C) 2020 Commown SCIC SAS (https://commown.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website sale promotion rule',
    'category': 'Website',
    "summary": "Use sale promotion rule on the website",
    'version': '10.0.0.0.1',
    "author": "Commown SCIC SAS, Akretion, Odoo Community Association (OCA)",
    'license': "AGPL-3",
    "website": "https://github.com/OCA/website",
    'depends': [
        'website_sale',
        'sale_promotion_rule',
    ],
    'data': [
        "views/website.xml",
    ],
    'installable': True,
}
