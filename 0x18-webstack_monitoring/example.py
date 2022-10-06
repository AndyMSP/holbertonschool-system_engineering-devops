"""
Get all hosts for your organization returns "OK" response
"""

# DD_SITE="datadoghq.com" DD_API_KEY="cf8169d63c6f7716737545b15db2c0a0" DD_APP_KEY="7bcee8991b931b18cd379161eda4800324b19892" python3 "example.py"

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        # filter="env:ci",
    )

    print(response)