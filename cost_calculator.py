def calculate_costs(df):
    pricing = {
        'EC2': 0.023,        # per hour
        'S3': 0.023,         # per GB
        'Lambda': 0.0000002, # per invocation
        'RDS': 0.034         # per hour
    }

    cost_summary = {}

    for _, row in df.iterrows():
        service = row['service']
        if service == 'EC2' or service == 'RDS':
            cost = row['usage_hours'] * pricing[service]
        elif service == 'S3':
            cost = row['storage_gb'] * pricing[service]
        elif service == 'Lambda':
            cost = row['invocations'] * pricing[service]
        else:
            cost = 0
        cost_summary[service] = round(cost, 2)

    return cost_summary
