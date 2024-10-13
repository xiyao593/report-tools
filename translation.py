# 招商银行交易
from datetime import datetime


class CMBTransaction:
    field_list = ['账号', '账号名称', '币种', '交易日', '交易时间', '起息日', '交易类型', '借方金额', '贷方金额',
                  '余额', '摘要', '流水号', '流程实例号', '业务名称', '用途', '业务参考号', '业务摘要', '其它摘要',
                  '收(付)方分行名', '收(付)方名称'
                  ]

    def __init__(self, account_number, account_name, currency_type, transaction_date,
                 transaction_time, value_date, transaction_type, debit_amount,
                 credit_amount, balance, summary, serial_number, process_instance_number,
                 business_name, purpose, business_reference_number, business_summary, other_summary, shoufu_bank,
                 shoufu_name):
        # 账号
        self.account_number = account_number

        # 账号名称
        self.account_name = account_name

        # 币种
        self.currency_type = currency_type

        # 交易日
        self.transaction_date = datetime.strptime(transaction_date, "%Y-%m-%d").date()

        # 交易时间
        self.transaction_time = datetime.strptime(transaction_time, "%H:%M:%S").time()

        # 起息日
        self.value_date = datetime.strptime(value_date, "%Y-%m-%d").date()

        # 交易类型
        self.transaction_type = transaction_type

        # 借方金额
        self.debit_amount = debit_amount

        # 贷方金额
        self.credit_amount = credit_amount

        # 余额
        self.balance = balance

        # 摘要
        self.summary = summary

        # 流水号
        self.serial_number = serial_number

        # 流程实例号
        self.process_instance_number = process_instance_number

        # 业务名称
        self.business_name = business_name

        # 用途
        self.purpose = purpose

        # 业务参考号
        self.business_reference_number = business_reference_number

        # 业务摘要
        self.business_summary = business_summary

        # 其它摘要
        self.other_summary = other_summary

        # 收(付)方分行名
        self.shoufu_bank = shoufu_bank

        # 收(付)方名称
        self.shoufu_name = shoufu_name

    def __repr__(self):
        return f"Transaction(account_number={self.account_number}, account_name={self.account_name}, currency_type={self.currency_type}, transaction_date={self.transaction_date}, transaction_time={self.transaction_time}, value_date={self.value_date}, transaction_type={self.transaction_type}, debit_amount={self.debit_amount}, credit_amount={self.credit_amount}, balance={self.balance}, summary={self.summary}, serial_number={self.serial_number}, process_instance_number={self.process_instance_number}, business_name={self.business_name}, purpose={self.purpose}, business_reference_number={self.business_reference_number}, business_summary={self.business_summary}, shoufu_name={self.shoufu_name})"

    def convert(self):
        date = self.transaction_date
        original_currency_amount = self.balance
        rmb_amount = self.balance
        currency = 'CNY'
        description = self.summary
        payer = None
        payee = None
        revenue_or_expense = True
        business_entity = None
        purpose = None
        business_type = None
        posting_status = None
        remarks = None

        if "HUAWEI SERVICES (HONG KONG) CO" in self.shoufu_name:
            description = '华为结算款'


        return TransactionRecord(date=date,
                                 original_currency_amount=original_currency_amount,
                                 rmb_amount=rmb_amount,
                                 currency=currency,
                                 description=description,
                                 payer=payer,
                                 payee=payee,
                                 revenue_or_expense=revenue_or_expense,
                                 business_entity=business_entity,
                                 purpose=purpose,
                                 business_type=business_type,
                                 posting_status=posting_status,
                                 remarks=remarks)


# 汇总交易记录
class TransactionRecord:
    field_list = [
        "日期",
        "原币金额金额",
        "RMB金额",
        "币种",
        "描述",
        "打款方",
        "收款方",
        "收支",
        "业务主体",
        "用途",
        "业务类型",
        "入账状态",
        "备注"
    ]

    def __init__(self, date, original_currency_amount, rmb_amount, currency, description, payer, payee,
                 revenue_or_expense, business_entity, purpose, business_type, posting_status, remarks):
        self.date = date  # 日期
        self.original_currency_amount = original_currency_amount  # 原币金额
        self.rmb_amount = rmb_amount  # RMB金额
        self.currency = currency  # 币种
        self.description = description  # 描述
        self.payer = payer  # 打款方
        self.payee = payee  # 收款方
        self.revenue_or_expense = '支出' if revenue_or_expense else '收入'  # 收支
        self.business_entity = business_entity  # 业务主体
        self.purpose = purpose  # 用途
        self.business_type = business_type  # 业务类型
        self.posting_status = posting_status  # 入账状态
        self.remarks = remarks  # 备注

    def __repr__(self):
        return ("TransactionRecord(date={self.date}, original_currency_amount={self.original_currency_amount}, "
                "rmb_amount={self.rmb_amount}, currency={self.currency}, description={self.description}, "
                "payer={self.payer}, payee={self.payee}, revenue_or_expense={self.revenue_or_expense}, "
                "business_entity={self.business_entity}, purpose={self.purpose}, "
                "business_type={self.business_type}, posting_status={self.posting_status}, "
                "remarks={self.remarks})")
