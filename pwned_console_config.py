#!/usr/bin/python


# Config for banners
#----------------------------------------------------------------------
banners_path = '/root/pwned_console/banners/'
default_banner = '{}pwned_console_default.banner'.format(banners_path)
#----------------------------------------------------------------------

# List for storing TLD values to strip within description text
#----------------------------------------------------------------------
tld_strip_list = ['.com','.net','.org','.edu','.int','.co','.uk','.cn','.ru','.se','.ca','.gov','.biz','.be','.asia','.su','.cm','.is']
#----------------------------------------------------------------------

# Error message values
#----------------------------------------------------------------------
index_error_message = "[-]Missing argument."
value_error_message = "[-]Option not allowed."
usage_message = "[*]Usage: python pwnconsole.py <email_addr/account_name>"
