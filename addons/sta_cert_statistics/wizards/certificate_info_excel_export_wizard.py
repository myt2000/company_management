# -*- coding: utf-8 -*-

import xlwt
import StringIO
import base64
from datetime import datetime


from io import BytesIO


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError, UserError
import xlwt
import logging

class Certificate_excel_export(models.TransientModel):
    _name = 'certificate.info.excel.export.wizard'

    start_date = fields.Date(string="Start Time", default=fields.Date.context_today)
    # formal_access_date = fields.Date(string="Formal Access Search Date", default=fields.Date.context_today)
    end_date =fields.Date(string="End Time", default=fields.Date.context_today)
    file = fields.Binary('Export File')

    # @api.multi
    # def export_all_excel_data(self):
    #     data = self.data_collation_all(self.title())
    #     self.file = self.create_excel(data)
    #
    #     value = dict(
    #         type='ir.actions.act_url',
    #         target='new',
    #         url='/web/content?model=%s&id=%s&field=file&download=true&filename=%s-%ssta发证信息统计.xlsx' % (
    #         self._name, self.id, self.start_date, self.end_date),
    #     )
    #     return value
    #
    # def data_collation_all(self, title):
    #     access_info = self.env['certificate.info'].search(([]), order='date desc')
    #
    #     # formal_info = self.env['company.info'].search(([()]))
    #     export_data = [title]
    #     for current_info in access_info:
    #         single_export_data = []
    #         single_export_data.append(self.company_name_hanler(current_info))
    #         single_export_data.append(self.company_abbreviation_handler(current_info))
    #         single_export_data.append(self.product_name_handler(current_info))
    #         single_export_data.append(self.status_handler(current_info))
    #         single_export_data.append(self.access_date_handler(current_info))
    #         single_export_data.append(self.formal_access_date_handler(current_info))
    #         single_export_data.append(self.company_level_id_handler(current_info))
    #         single_export_data.append(self.mail_handler(current_info))
    #         single_export_data.append(self.version_id_handler(current_info))
    #         single_export_data.append(self.saler_id_handler(current_info))
    #         single_export_data.append(self.demo_address_handler(current_info))
    #         single_export_data.append(self.platform_handler(current_info))
    #         single_export_data.append(self.product_handler(current_info))
    #         single_export_data.append(self.third_party_handler(current_info))
    #         single_export_data.append(self.support_specialist_id_handler(current_info))
    #         single_export_data.append(self.certificate_name_handler(current_info))
    #         single_export_data.append(self.common_name_handler(current_info))
    #         single_export_data.append(self.effective_time_handler(current_info))
    #         single_export_data.append(self.package_name_id_handler(current_info))
    #         single_export_data.append(self.extra_function_id_hanlder(current_info))
    #         single_export_data.append(self.remark_handler(current_info))
    #         single_export_data.append(self.contact_info_handler(current_info))
    #         export_data.append(single_export_data)
    #     return export_data

    @api.multi
    def export_excel_data(self):
        # support_specialist = [int(x) for x in self.support_specialist_id]
        # logging.info(support_specialist)
        # today = datetime.now().strftime('%Y-%m-%d')
        start_date = self.start_date
        end_date = self.end_date
        # formal_access_date = self.formal_access_date
        if start_date > end_date :
            raise UserError(_("The query date cannot be greater than the start day!"))
        logging.info("start_date: %s" % start_date)
        logging.info("end_data: %s" % start_date)
        data = self.data_collation(start_date, end_date, self.title())
        self.file = self.create_excel(data)

        value = dict(
            type='ir.actions.act_url',
            target='new',
            url='/web/content?model=%s&id=%s&field=file&download=true&filename=%s-%s_STA发证信息统计.xlsx' % (self._name, self.id, start_date, end_date),
        )
        return value


    def create_excel(self, data):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('sta发证信息统计')
        for i in range(len(data)):
            for j in range(len(data[i])):
                worksheet.write(i, j, data[i][j])

        buffer = BytesIO()
        logging.info(buffer)
        workbook.save(buffer)

        return base64.b64decode(buffer.getvalue())



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

#
# '''
# 发证日期
# 公司名称
# 功能
# 平台
# 证书状态
# 发证时长
# 备注
# '''
    def title(self):
        return ['发证日期', '公司名称', '功能', '平台', '证书状态', '发证时长', '发证人', '备注']

    def data_collation(self, start_date,  end_data, title):
        access_info = self.env['certificate.info'].search(([('date', '>=', start_date),
                                                        ('date', '<=', end_data),]), order='status')
        logging.info(start_date)
        logging.info(end_data)
        # formal_info = self.env['company.info'].search(([()]))
        export_data = [title]
        for current_info in access_info:
            single_export_data = []
            single_export_data.append(self.date_handler(current_info))
            single_export_data.append(self.company_name_hanler(current_info))
            single_export_data.append(self.function_handler(current_info))
            single_export_data.append(self.status_handler(current_info))
            single_export_data.append(self.platform_handler(current_info))
            single_export_data.append(self.days_handler(current_info))
            single_export_data.append(self.support_specialist_id_handler(current_info))
            single_export_data.append(self.remark_handler(current_info))

            export_data.append(single_export_data)
        # export_data.append(self.data_statistics(access_date, support_specialist))
        return export_data



    # def data_statistics(self, access_date, support_specialist):
    #     formal_num = self.env['company.info'].search_count((['&', '&', ('support_specialist_id.id', 'in', support_specialist), ('status', '=', 'formal'), '|', ('formal_access_date', '>=', access_date), ('access_date', '>=', access_date), ]))
    #     test_num = self.env['company.info'].search_count((['&', '&', ('support_specialist_id.id', 'in', support_specialist), ('status', '=', 'test'), '|', ('formal_access_date', '>=', access_date), ('access_date', '>=', access_date),]))
    #     abort_num = self.env['company.info'].search_count((['&', '&', ('support_specialist_id.id', 'in', support_specialist), ('status', '=', 'abort'), '|', ('formal_access_date', '>=', access_date), ('access_date', '>=', access_date),]))
    #     status_list = ['正式客户：', formal_num, '测试客户：', test_num, '停用客户', abort_num]
    #     return status_list


    def date_handler(self, info):
        if info.date:
            return info.date
        return

    def company_name_hanler(self, info):
        if info.company_name:
            return info.company_name
        return



    def function_handler(self, info):
        if info.function:
            return info.function
        return

    def status_handler(self, info):
        status_translation = {'formal': '正式', 'test': '测试', 'abort': '停用'}
        if info.status:
            return status_translation[info.status]
        return None

    def platform_handler(self, info):
        if len(info.platform):
            platform_list = []
            for single in info.platform:
                platform_list.append(single.name)
            return ','.join(platform_list)
        return

    def days_handler(self, info):
        if info.days:
            return info.days
        return

    def support_specialist_id_handler(self, info):
        if len(info.support_specialist_id):
            support_specialist_id_list = []
            for support_specialist in info.support_specialist_id:
                support_specialist_id_list.append(support_specialist.name)
            return ','.join(support_specialist_id_list)
        return



    def remark_handler(self, info):
        if info.remark:
            return info.remark
        return






    # @property
    # def content_type(self):
    #     return 'application/vnd.ms-excel'
    #
    # def filename(self, base):
    #     return base + '.xlsx'