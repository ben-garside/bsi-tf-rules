from lark import Token

from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories
import re

VM_NAME_RULE = re.compile('(BSI)-(UKS|UKW)-(PROD|DEV|TEST|UAT|QA)-(.*)-(.*)')

class VMNamePolicy(BaseResourceCheck):
    def __init__(self):
        name = "Ensure VM meet BSI naming rules"
        id = "BSI_AZURE_001"
        supported_resources = ['azurerm_virtual_machine']
        # CheckCategories are defined in models/enums.py
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for the name of the VM and checks against policy
        :param conf: name 
        :return: <CheckResult>
        """
        if 'name' in conf:
            vm_name = conf['name'][0]
            if not re.match(VM_NAME_RULE, vm_name): 
                return CheckResult.FAILED
        return CheckResult.PASSED


scanner = VMNamePolicy()