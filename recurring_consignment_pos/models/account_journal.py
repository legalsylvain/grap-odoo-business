# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.constrains("type")
    def _check_type(self):
        if self.env.context.get("install_filename", "").endswith(
            "recurring_consignment_pos/demo/account_journal.xml"
        ):
            return
        return super()._check_type()
