# coding=utf-8
import hashlib


class CollectionsManager(object):
    def __init__(self):
        """"Constructor for Collection class.

        self.collections is a dict of collection with this structure:
        self.collections = {
            collection_id (computed): {
                'author': author,
                'author_email': email,
                'repository_url': self.url,
                'name': parser.get(collection, 'name'),
                'tags': parser.get(collection, 'tags'),
                'description': parser.get(collection, 'description'),
                'qgis_min_version': parser.get(collection, 'qgis_minimum_version'),
                'qgis_max_version': parser.get(collection, 'qgis_maximum_version')
            },
            ....
        }

        self.repo_collections is a list dict of collection with this structure:
        self.repo_collection = {
            repo_name: [{
                'author': author,
                'author_email': email,
                'repository_url': self.url,
                'name': parser.get(collection, 'name'),
                'tags': parser.get(collection, 'tags'),
                'description': parser.get(collection, 'description'),
                'qgis_min_version': parser.get(collection, 'qgis_minimum_version'),
                'qgis_max_version': parser.get(collection, 'qgis_maximum_version')
            },
            ....
        }

        They are separated for different operation. self.collections is to
        deal with each collection (downloading, browsing, searching,
        etc). Self.repo_collection is to deal with adding, updating, removing repository.
        """
        self._collections = {}
        self._repo_collections = {}

    @property
    def collections(self):
        return self._collections

    @property
    def repo_collections(self):
        return self._repo_collections

    def add_repo_collection(self, name, collections):
        """Add repo collections.

        :param name: The name of the repository.
        :type name: str

        :param collections: The list of collections.
        :type collections: list
        """
        self.repo_collections[name] = collections

    def remove_repo_collection(self, name):
        """Remove a repo collection by name from repo collections."""
        self.repo_collections.pop(name, None)

    def rebuild_collections(self):
        """Rebuild collections from repo collections."""
        self._collections = {}
        for repo in self._repo_collections.keys():
            repo_collections = self.repo_collections[repo]
            for collection in repo_collections:
                colection_id = self.get_collection_id(
                    collection['name'], collection['repository_url'])
                self._collections[colection_id] = collection

    def get_collection_id(self, collection_name, repo_url):
        """Generate id of a collection."""
        hash_object = hashlib.sha1(collection_name + repo_url)
        hex_dig = hash_object.hexdigest()
        return hex_dig



