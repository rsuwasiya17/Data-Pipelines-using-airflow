from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import logging

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 dq_test = "",
                 tables = [],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.tables = tables
        self.redshift_conn_id = redshift_conn_id
        self.dq_test = dq_test

    def execute(self, context):
        redshift_hook = PostgresHook(self.redshift_conn_id)
        for test in self.dq_test:
            sql = check.get('test_sql')
            exp_result = check.get('expected_result')
            records_query = redshift.get_records(sql)[0]
            if exp_result != records_query[0]:
                error_count += 1
                failed_tests.append(sql)
        if error_count > 0:
            self.log.info('Tests failed')
            self.log.info(failed_tests)
            raise ValueError('Data quality check failed')
        for table in self.tables:
            self.log.info(f"Data Quality for {table} table")
            records = redshift_hook.get_records(f"SELECT COUNT(*) from {table}")
            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError(f"Data quality check failed. {table} returned no results")
            num_records = records[0][0]
            if num_records < 1:
                raise ValueError(f"Data quality check failed. {table} contained 0 rows")
            self.log.info(f"Data quality on table {table} check passed with {records[0][0]} records")
