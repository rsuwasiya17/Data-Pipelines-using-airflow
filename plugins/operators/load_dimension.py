from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import logging

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 load_sql_stmt= "",
                 append = False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.load_sql_stmt = load_sql_stmt
        self.append = append

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        self.log.info(f"Loading dimension table {self.table}")
        sql = ""
        if self.append:
            f_sql = """
                    BEGIN;
                    INSERT INTO {}
                    {};
                    COMMIT;""".format(self.table, self.load_sql_stmt)
        else:
            f_sql = """
                    BEGIN;
                    TRUNCATE TABLE {};
                    INSERT INTO {}
                    {};
                    COMMIT;""".format(self.table,self.table,self.load_sql_stmt)
        
        redshift.run(f_sql)                 
