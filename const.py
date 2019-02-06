# Copyright (c) 2018, WSO2 Inc. (http://wso2.com) All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

NS = {'d': 'http://maven.apache.org/POM/4.0.0'}
ZIP_FILE_EXTENSION = ".zip"
CARBON_NAME = "carbon.zip"
VALUE_TAG = "{http://maven.apache.org/POM/4.0.0}value"
SURFACE_PLUGIN_ARTIFACT_ID = "maven-surefire-plugin"
DATASOURCE_PATHS = {"product-iots": {
    "CORE": ["conf/datasources/master-datasources.xml", "conf/datasources/cdm-datasources.xml",
             "conf/datasources/android-datasources.xml"],
    "BROKER": [],
    "ANALYTICS": []},
                    }
M2_PATH = {"product-iots": "iot/wso2iot"}
DIST_POM_PATH = {"product-is": "modules/distribution/pom.xml", "product-apim": "modules/distribution/product/pom.xml",
                 "product-ei": "distribution/pom.xml"}
LIB_PATH = "lib"
DISTRIBUTION_PATH = {"product-apim": "modules/distribution/product/target",
                     "product-is": "modules/distribution/target",
                     "product-ei": "distribution/target"}
PRODUCT_STORAGE_DIR_NAME = "product"
TEST_PLAN_PROPERTY_FILE_NAME = "testplan-props.properties"
INFRA_PROPERTY_FILE_NAME = "infrastructure.properties"
LOG_FILE_NAME = "integration.log"
ORACLE_DB_ENGINE = "ORACLE-SE2"
MSSQL_DB_ENGINE = "SQLSERVER-SE"
MYSQL_DB_ENGINE = "MYSQL"
DEFAULT_ORACLE_SID = "orcl"
DEFAULT_DB_USERNAME = "wso2carbon"
LOG_STORAGE = "logs"
LOG_FILE_PATHS = {"product-apim": [],
                  "product-is": [],
                  "product-ei": []}
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar",
              "DB_SETUP": {
                  "product-apim": {},
                  "product-is": {},
                  "product-ei": {},
                  "product-iots": {"WSO2_CARBON_DB_CORE": ['dbscripts/mysql5.7.sql'],
                                   "WSO2APPM_DB_CORE": ['dbscripts/appmgt/mysql5.7.sql'],
                                   "WSO2AM_DB_CORE": ['dbscripts/apimgt/mysql5.7.sql'],
                                   "WSO2_MB_STORE_DB_CORE": ['wso2/broker/dbscripts/mb-store/mysql-mb.sql'],
                                   "JAGH2_CORE": ['dbscripts/mysql5.7.sql'],
                                   "WSO2_SOCIAL_DB_CORE": ['dbscripts/social/mysql/resource.sql'],
                                   "DM_DS_CORE": ['dbscripts/cdm/mysql.sql'],
                                   "DM_ARCHIVAL_DS_CORE": ['dbscripts/cdm/mysql.sql'],
                                   "Android_DB_CORE": ['dbscripts/cdm/plugins/android/mysql.sql']}}},

    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar",
                     "DB_SETUP": {
                         "product-apim": {},
                         "product-is": {},
                         "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/mssql.sql'],
                                        "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/mssql.sql'],
                                        "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/mssql.sql'],
                                        "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/mssql-mb.sql'],
                                        "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/mssql.sql'],
                                        "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/mssql.sql'],
                                        "ACTIVITI_DB_BPS": [
                                            'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.identity.sql']}}},

    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar",
                   "DB_SETUP": {
                       "product-apim": {},
                       "product-is": {},
                       "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/oracle.sql'],
                                      "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/oracle.sql'],
                                      "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/oracle.sql'],
                                      "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/oracle-mb.sql'],
                                      "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/oracle.sql'],
                                      "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/oracle.sql'],
                                      "ACTIVITI_DB_BPS": [
                                          'wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.identity.sql']}}},

    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar",
                   "DB_SETUP": {"product-apim": {},
                                "product-is": {},
                                "product-ei": {}}
                   }}
