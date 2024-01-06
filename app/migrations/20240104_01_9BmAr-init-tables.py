"""
init tables
"""

from yoyo import step

__depends__ = {}

steps = [
    step(''' 
        CREATE TABLE lead_table (
            id serial PRIMARY KEY,
            request_id varchar(255),
            lead_name varchar(255),
            create_time timestamp WITH TIME ZONE NOT NULL DEFAULT NOW(),
            meet_time timestamp,
            site_name varchar(255),
            account varchar(255),
            direction varchar(255),
            city varchar(255),
            statuses varchar(255),
            place varchar(255),
            description varchar(255),
            fiat_amount varchar(255),
            crypto_amount varchar(255),
            percent varchar(255),
            exchange_rate varchar(255),
            exchageType varchar(255),
            wallet varchar(255),
            card_number varchar(255),           
            platform varchar(255),
            billColor varchar(255),
            client_type varchar(255),
            form_type varchar(255),
            client_class varchar(255),
            crm_lead_id integer
        );
    
    '''),
    step(''' 
         CREATE TABLE if not exists clients_table (
                        id serial PRIMARY KEY,
                        name varchar(255),
                        kit_value boolean,
                        date_add_kit timestamp
                    );
    ''')
]
