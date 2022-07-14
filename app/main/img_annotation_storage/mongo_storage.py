from .. import mongo
import codecs
from gridfs import GridFS
from bson.json_util import dumps
from ..img_annotation_exception.img_ann_exception import *


class MongoStorage:

    def __init__(self, base_collection):
        self.mongo_db = mongo.db
        self.mongo_cl = mongo.db[base_collection]

    def find_all(self):
        data_sets = self.mongo_cl.find()
        resp = dumps(data_sets)
        return resp

    def find_all_by_query(self, query):
        result_sets = self.mongo_cl.find(query)
        return dumps(result_sets)

    def find_one(self, data_set_id):
        data_set = self.mongo_cl.find_one({'data_set_id': data_set_id})
        return dumps(data_set)

    def update_one(self, data_set_id, new_ds):
        old_data_set = self.mongo_cl.find_one({'data_set_id': data_set_id})
        data_sets = self.mongo_cl.find()
        resp = dumps(data_sets)
        return resp

    def update_all(self, data_set_id, new_ds):
        old_data_set = self.mongo_cl.find_one({'data_set_id': data_set_id})
        data_sets = self.mongo_cl.find()
        resp = dumps(data_sets)
        return resp

    def save_all(self, data):
        inserted = False
        try:
            self.mongo_cl.insert_many(data)
            inserted = True
        except mongo.errors.ConnectionFailure as e:
            raise ImgAnnAPIException(' Error while connecting db  %s', base_exception=e)
        except mongo.errors.BulkWriteError as e:
            raise ImgAnnAPIException(' Error while data insertion %s', e)
        except Exception as e:
            raise ImgAnnAPIException(' Error while data insertion %s', e)
        return inserted

    def save_one(self, data):
        inserted = False
        try:
            self.mongo_cl.insert_one(data)
            inserted = True
        except mongo.errors.ConnectionFailure as e:
            raise ImgAnnAPIException(' Error while connecting db  %s', base_exception=e)
        except Exception as e:
            raise ImgAnnAPIException(' Error while data insertion %s', base_exception=e)

        return inserted

    def save_one_img(self, image, img_name, img_dsc):
        inserted = False
        try:
            grid_fs = GridFS(self.mongo_db)
            img_id = grid_fs.put(image,  filename = img_name)
            img = {}
            img["img_id"] = img_id
            img["img_name"] = img_name
            img["img_dsc"] = img_dsc
            self.mongo_cl.insert_one(img)
            inserted = True
        except mongo.errors.ConnectionFailure as e:
            raise ImgAnnAPIException(' Error while connecting db  %s', base_exception=e)
        except Exception as e:
            raise ImgAnnAPIException(' Error while data insertion %s', base_exception=e)

        return inserted

    def find_one_img(self, img_id, img_name):
        image = ''
        try:
            query = {}
            if img_name != '' and img_id != '':
                query = {'img_name': img_name, 'img_id':img_id}
            elif img_id != '':
                query = {'img_name': img_name}
            elif img_id != '':
                query = {'img_id': img_id}
            print("img query is ", query)
            img = self.mongo_cl.find_one(query)
            grid_fs = GridFS(self.mongo_db)
            image = grid_fs.get(img['img_id'])
            base64_data = codecs.encode(image.read(), 'base64')
            image = base64_data.decode('utf-8')
        except mongo.errors.ConnectionFailure as e:
            raise ImgAnnAPIException(' Error while connecting db  %s', base_exception=e)
        except Exception as e:
            raise ImgAnnAPIException(' Error while data insertion %s', base_exception=e)

        return {"img_name":img['img_name'], "image":image}

    def find_all_img(self, img_id, img_name):
        image = ''
        try:
            query = {}
            if img_name != '' and img_id != '':
                query = {'img_name': img_name, 'img_id':img_id}
            elif img_id != '':
                query = {'img_name': img_name}
            elif img_id != '':
                query = {'img_id': img_id}
            print("img query is ", query)
            images = self.mongo_cl.find(query)
            image_list = []
            for img in images:
                grid_fs = GridFS(self.mongo_db)
                image = grid_fs.get(img['img_id'])
                base64_data = codecs.encode(image.read(), 'base64')
                image = base64_data.decode('utf-8')
                image_list.append({"img_name":img['img_name'], "image":image})

        except mongo.errors.ConnectionFailure as e:
            raise ImgAnnAPIException(' Error while connecting db  %s', base_exception=e)
        except Exception as e:
            raise ImgAnnAPIException(' Error while data insertion %s', base_exception=e)

        return image_list
