from cgi import print_form
import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ydc23824;PWD=RHxHgH1rnTluiY9S", '','')

print(conn)
print("connection successful...")
