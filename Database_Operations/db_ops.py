# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider
# import csv


class db_ops:
    """
        This class shall be used for importing the data and exporting

        Written By: Suraj Joshi
        Version: 1.0
        Revisions: None

    """

    def __init__(self, logger, path):
        try:
            self.log = logger
            self.path = path

            # cloud_config = {
            #     'secure_connect_bundle': './secure-connect-spam-ham.zip'
            # }
            # auth_provider = PlainTextAuthProvider('bTiAqRLnWXBnromkirhAZgEf',
            #                                       'gTH.dBpX++UfrT-2Lpw++Zgz0d1zPbA2LzyHnZskSQ1HfBwFs7C2.'
            #                                       'uy6b2EnIzPMZHf5Q33nKN.mZOZ+2-Kni_q-Ttf0y1ZF2P+ncdGMtzSdQKeKWF'
            #                                       'atvKpyc,KMlrvY')
            # cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            # self.session = cluster.connect()
            #
            # self.session.execute(""" CREATE TABLE if not exists training.all_train_files(
            #         id INT PRIMARY KEY,target text,text text,V1 text,V2 text,
            #         V3 text);""")
            #
            # self.session.execute('use training;')
            self.log.info('Object of db_ops initialized successfully')

        except Exception as e:
            self.log.warning('Exception occurred while object initialization in db_ops {}'.format(e))
            raise Exception

    def uploading_data(self):
        try:
            # csv_reader = csv.reader(open(self.path))
            # next(csv_reader)
            #
            # for rows in csv_reader:
            #     query = """INSERT INTO training.all_train_files(Id,target,text,V1,V2 ,V3)
            #     VALUES('%d','%s','%s','%s','%s','%s');""" % (
            #         int(rows[0]), str(rows[1]), str(rows[2]), str(rows[3]), str(rows[4]), str(rows[5]))
            #     self.session.execute(query)
            self.log.info('Data Uploaded Successfully')

        except Exception as e:
            self.log.warning('Exception occurred inside uploading_data in db_ops {}'.format(e))
            raise Exception

    def extracting_data(self):
        try:
            main_train_data_path = 'Training_file.csv'
            # f = open(main_train_data_path, 'w', encoding='utf8')
            # f.truncate()
            # writer = csv.writer(f)
            #
            # # Writing the column names
            # writer.writerow(tuple(['Id', 'target', 'text', 'V1', 'V2', 'V3']))
            # for val in self.session.execute('select * from training.all_train_files;'):
            #     row = [
            #         val.Id, val.target, val.text, val.V1, val.V2, val.V3]
            #     # write each row to the csv file
            #     writer.writerow(tuple(row))
            #
            # f.close()
            self.log.info('Retrieving data from DB Completed and stored in {}'.format(main_train_data_path))
            return main_train_data_path

        except Exception as e:
            self.log.warning('Exception occurred inside extracting_data in db_ops {}'.format(e))
            raise Exception

    def start_db(self):
        self.uploading_data()
        train_path = self.extracting_data()
        return train_path
