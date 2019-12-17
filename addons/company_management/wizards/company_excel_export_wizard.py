# -*- coding: utf-8 -*-

import xlwt
import StringIO
import base64
from datetime import datetime


from io import BytesIO


from odoo import  models, fields, api
from odoo.exceptions import ValidationError, AccessError, UserError
import xlwt
import logging

class Company_excel_export(models.TransientModel):
    _name = 'company.excel.export.wizard'

    def _get_default_support_specialist(self):
        return self.env['res.users'].search([('id', '=', self.env.uid)])

    access_date = fields.Date(string="Access Search Time", default=fields.Date.context_today)
    # formal_access_date = fields.Date(string="Formal Access Search Date", default=fields.Date.context_today)
    support_specialist_id = fields.Many2many('res.users', 'info_res_users_wizard_rel', string="Support Specialist Choose",
                                             default=_get_default_support_specialist)
    file = fields.Binary('Export File')

    @api.multi
    def export_all_excel_data(self):
        data = self.data_collation_all(self.title())
        self.file = self.create_excel(data)

        value = dict(
            type='ir.actions.act_url',
            target='new',
            url='/web/content?model=%s&id=%s&field=file&download=true&filename=%s公司信息.xlsx' % (
            self._name, self.id, datetime.now().strftime('%Y-%m-%d')),
        )
        return value

    def data_collation_all(self, title):
        access_info = self.env['company.info'].search(([]), order='status')

        # formal_info = self.env['company.info'].search(([()]))
        export_data = [title]
        for current_info in access_info:
            single_export_data = []
            single_export_data.append(self.company_name_hanler(current_info))
            single_export_data.append(self.company_abbreviation_handler(current_info))
            single_export_data.append(self.product_name_handler(current_info))
            single_export_data.append(self.status_handler(current_info))
            single_export_data.append(self.access_date_handler(current_info))
            single_export_data.append(self.formal_access_date_handler(current_info))
            single_export_data.append(self.company_level_id_handler(current_info))
            single_export_data.append(self.mail_handler(current_info))
            single_export_data.append(self.version_id_handler(current_info))
            single_export_data.append(self.saler_id_handler(current_info))
            single_export_data.append(self.demo_address_handler(current_info))
            single_export_data.append(self.platform_handler(current_info))
            single_export_data.append(self.product_handler(current_info))
            single_export_data.append(self.third_party_handler(current_info))
            single_export_data.append(self.support_specialist_id_handler(current_info))
            single_export_data.append(self.certificate_name_handler(current_info))
            single_export_data.append(self.common_name_handler(current_info))
            single_export_data.append(self.effective_time_handler(current_info))
            single_export_data.append(self.package_name_id_handler(current_info))
            single_export_data.append(self.extra_function_id_hanlder(current_info))
            single_export_data.append(self.remark_handler(current_info))
            single_export_data.append(self.contact_info_handler(current_info))
            export_data.append(single_export_data)
        return export_data

    @api.multi
    def export_excel_data(self):
        support_specialist = [int(x) for x in self.support_specialist_id]
        logging.info(support_specialist)
        today = datetime.now().strftime('%Y-%m-%d')
        access_date = self.access_date
        # formal_access_date = self.formal_access_date
        if access_date > today :
            raise UserError(_("The query date cannot be greater than the current day!"))
        elif not support_specialist:
            raise UserError(_("User must be selected"))
        logging.info(support_specialist)
        data = self.data_collation(access_date, support_specialist, self.title())
        self.file = self.create_excel(data)

        value = dict(
            type='ir.actions.act_url',
            target='new',
            url='/web/content?model=%s&id=%s&field=file&download=true&filename=%s公司信息.xlsx' % (self._name, self.id, today),
        )
        return value


    def create_excel(self, data):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('公司客户信息')
        for i in range(len(data)):
            for j in range(len(data[i])):
                worksheet.write(i, j, data[i][j])
        buffer = BytesIO()
        workbook.save(buffer)
        return base64.encodestring(buffer.getvalue())



    # def content_disposition(self, filename):
    #     """
    #     把参数拼接成excel的名
    #     :param filename: 文件名
    #     :return: attachment(拼接excel名)
    #     """
    #     filename = odoo.tools.ustr(filename)
    #     escaped = urllib2.quote(filename.encode('utf8'))
    #     browser = request.httprequest.user_agent.browser
    #     version = int((request.httprequest.user_agent.version or '0').split('.')[0])
    #     if browser == 'msie' and version < 9:
    #         return "attachment; filename=%s" % escaped
    #     elif browser == 'safari' and version < 537:
    #         return u"attachment; filename=%s" % filename.encode('ascii', 'replace')
    #     else:
    #         return "attachment; filename*=UTF-8''%s" % escaped

    # def file_title(self):
    #     return '{}公司信息'.format(datetime.now().strftime('%Y-%m-%d'))

    def title(self):
        return ['公司名称', '简称', '产品名称', '状态', '接入时间', '正式接入时间', '客户等级', '邮箱', '版本', '销售人员', 'Demo地址链接',
                '使用平台', '使用产品信息', '第三方', '技术支持专员', '证书名称', 'Common Name', '证书有效时间', '套餐', '额外功能', '备注', '联系信息',]

    def data_collation(self, access_date,  support_specialist, title):
        access_info = self.env['company.info'].search((['&', ('access_date', '>=', access_date), ('support_specialist_id.id', 'in', support_specialist),]), order='status')
        logging.info(access_date)
        # formal_info = self.env['company.info'].search(([()]))
        export_data = [title]
        for current_info in access_info:
            single_export_data = []
            single_export_data.append(self.company_name_hanler(current_info))
            single_export_data.append(self.company_abbreviation_handler(current_info))
            single_export_data.append(self.product_name_handler(current_info))
            single_export_data.append(self.status_handler(current_info))
            single_export_data.append(self.access_date_handler(current_info))
            single_export_data.append(self.formal_access_date_handler(current_info))
            single_export_data.append(self.company_level_id_handler(current_info))
            single_export_data.append(self.mail_handler(current_info))
            single_export_data.append(self.version_id_handler(current_info))
            single_export_data.append(self.saler_id_handler(current_info))
            single_export_data.append(self.demo_address_handler(current_info))
            single_export_data.append(self.platform_handler(current_info))
            single_export_data.append(self.product_handler(current_info))
            single_export_data.append(self.third_party_handler(current_info))
            single_export_data.append(self.support_specialist_id_handler(current_info))
            single_export_data.append(self.certificate_name_handler(current_info))
            single_export_data.append(self.common_name_handler(current_info))
            single_export_data.append(self.effective_time_handler(current_info))
            single_export_data.append(self.package_name_id_handler(current_info))
            single_export_data.append(self.extra_function_id_hanlder(current_info))
            single_export_data.append(self.remark_handler(current_info))
            single_export_data.append(self.contact_info_handler(current_info))
            export_data.append(single_export_data)
        export_data.append(self.data_statistics(access_date, support_specialist))
        return export_data



    def data_statistics(self, access_date, support_specialist):
        formal_num = self.env['company.info'].search_count((['&', '&', ('access_date', '>=', access_date), ('support_specialist_id.id', 'in', support_specialist), ('status', '=', 'formal')]))
        test_num = self.env['company.info'].search_count((['&', '&', ('access_date', '>=', access_date), ('support_specialist_id.id', 'in', support_specialist), ('status', '=', 'test')]))
        abort_num = self.env['company.info'].search_count((['&', '&', ('access_date', '>=', access_date), ('support_specialist_id.id', 'in', support_specialist), ('status', '=', 'abort')]))
        status_list = ['正式客户：', formal_num, '测试客户：', test_num, '停用客户', abort_num]
        return status_list


    def company_name_hanler(self, info):
        if info.company_name:
            return info.company_name
        return

    def company_abbreviation_handler(self, info):
        if info.company_abbreviation:
            return info.company_abbreviation
        return

    def product_name_handler(self, info):
        if info.product_name:
            return info.product_name
        return

    def status_handler(self, info):
        status_translation = {'formal': '正式', 'test': '测试', 'abort': '停用'}
        if info.status:
            return status_translation[info.status]
        return None

    def access_date_handler(self, info):
        if info.access_date:
            return info.access_date
        return

    def formal_access_date_handler(self, info):
        if info.formal_access_date:
            return info.formal_access_date
        return

    def mail_handler(self, info):
        if info.mail:
            return info.mail
        return

    def version_id_handler(self, info):
        if info.version_id:
            return info.version_id.name
        return

    def certificate_name_handler(self, info):
        if info.certificate_name:
            return info.certificate_name
        return

    def common_name_handler(self, info):
        if info.common_name:
            return info.common_name
        return

    def package_name_id_handler(self, info):
        if len(info.package_name_id):
            package_list = []
            for package in info.package_name_id:
                package_list.append(package.name)
            return ','.join(package_list)
        return

    def extra_function_id_hanlder(self, info):
        if len(info.extra_function_id):
            extra_list = []
            for extra in info.extra_function_id:
                extra_list.append(extra.name)
            return ','.join(extra_list)
        return

    def company_level_id_handler(self, info):
        if info.company_level_id:
            return info.company_level_id.name
        return

    def saler_id_handler(self, info):
        if info.saler_id:
            return info.saler_id.name
        return

    def platform_handler(self, info):
        if len(info.platform):
            platform_list = []
            for single in info.platform:
                platform_list.append(single.name)
            return ','.join(platform_list)
        return

    def product_handler(self, info):
        if len(info.product):
            product_list = []
            for single in info.product:
                product_list.append(single.name)
            return ','.join(product_list)
        return

    def support_specialist_id_handler(self, info):
        if len(info.support_specialist_id):
            support_specialist_id_list = []
            for support_specialist in info.support_specialist_id:
                support_specialist_id_list.append(support_specialist.name)
            return ','.join(support_specialist_id_list)
        return

    def contact_info_handler(self, info):
        if len(info.contact_info):
            contact_info_list = []
            for single in info.contact_info:
                if isinstance(single.name, str):
                    contact_info_list.append(single.name)
                else:
                    contact_info_list.append('')
            return ','.join(contact_info_list)
        return

    def remark_handler(self, info):
        if info.remark:
            return info.remark
        return

    def effective_time_handler(self, info):
        if info.effective_time:
            return info.effective_time
        return

    def demo_address_handler(self, info):
        if info.demo_address:
            return info.demo_address
        return

    def third_party_handler(self, info):
        if len(info.third_party):
            third_party_list = []
            for single in info.third_party:
                third_party_list.append(single.name)
            return ','.join(third_party_list)
        return


    # @property
    # def content_type(self):
    #     return 'application/vnd.ms-excel'
    #
    # def filename(self, base):
    #     return base + '.xlsx'