# 招商银行交易
class CMBTransaction:
    field_list = ['账号', '账号名称', '币种', '交易日', '交易时间', '起息日', '交易类型', '借方金额', '贷方金额',
                  '余额', '摘要', '流水号', '流程实例号', '业务名称', '用途', '业务参考号', '业务摘要']

    def __init__(self, account_number, account_name, currency_type, transaction_date,
                 transaction_time, value_date, transaction_type, debit_amount,
                 credit_amount, balance, summary, serial_number, process_instance_number,
                 business_name, purpose, business_reference_number, business_summary):
        # 账号
        self.account_number = account_number

        # 账号名称
        self.account_name = account_name

        # 币种
        self.currency_type = currency_type

        # 交易日
        self.transaction_date = transaction_date

        # 交易时间
        self.transaction_time = transaction_time

        # 起息日
        self.value_date = value_date

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

    def __repr__(self):
        return f"Transaction(account_number={self.account_number}, account_name={self.account_name}, currency_type={self.currency_type}, transaction_date={self.transaction_date}, transaction_time={self.transaction_time}, value_date={self.value_date}, transaction_type={self.transaction_type}, debit_amount={self.debit_amount}, credit_amount={self.credit_amount}, balance={self.balance}, summary={self.summary}, serial_number={self.serial_number}, process_instance_number={self.process_instance_number}, business_name={self.business_name}, purpose={self.purpose}, business_reference_number={self.business_reference_number}, business_summary={self.business_summary})"
