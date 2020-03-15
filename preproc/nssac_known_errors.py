from preproc.known_error import KnownCSVError, KnownErrors


nssac_known_errors = KnownErrors()
nssac_known_errors.add(KnownCSVError('nssac-ncov-sd-02-24-2020.csv', "Hunan,Mainland China,2020-02-25 03:00:00,1016,4,751", linenr=6))
nssac_known_errors.add(KnownCSVError('nssac-ncov-sd-02-24-2020.csv', "Sichuan,Mainland China,2020-02-25 03:00:00,529,3,278", linenr=12))
nssac_known_errors.add(KnownCSVError('nssac-ncov-sd-02-24-2020.csv', "Fujian,Mainland China,2020-02-25 03:00:00,294,1,188", linenr=17))
nssac_known_errors.add(KnownCSVError('nssac-ncov-sd-02-24-2020.csv', "Hainan,Mainland China,2020-02-25 03:00:00,168,5,116", linenr=21))
nssac_known_errors.add(KnownCSVError('nssac-ncov-sd-02-24-2020.csv', "Hong Kong,Hong Kong,2020-02-25 03:00:00,81,2,19", linenr=28))
nssac_known_errors.add(KnownCSVError('nssac-ncov-sd-02-24-2020.csv', "Unknown location US,USA,2020-02-24 12:00:00,36,0,0", linenr=68))

