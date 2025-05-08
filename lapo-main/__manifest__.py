# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'lapo',
    'version': '1.0',
    'summary': 'Procurment Workflow Process',
    'website': 'https://www.esnformatic.com',
    'author': 'ESN FORMTIC SARL',
    'description': """
        Procurment Workflow Process
    """,
    'category': 'Bqnk',
    'depends': [],
   
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        # 'data/paperformat.xml',
        # 'report/report.xml',
        # 'report/reportresultat.xml',
        # 'report/reportresultat2.xml',
        # 'report/reportrecu.xml',
        # 'report/reportbilan.xml',
        # 'report/reportfacture.xml',
        # 'report/reportarticle.xml',
        # 'report/reportetatstock.xml',
        # 'views/params.xml',
        'views/main.xml',
        'views/menu.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
