from eventsourcing.tests.example_application_tests.base import ExampleApplicationTestCase
from eventsourcing.tests.sequenced_item_repository_tests.test_cassandra_sequence_repository import \
    CassandraRepoTestCase


class TestExampleApplicationWithCassandra(CassandraRepoTestCase, ExampleApplicationTestCase):
    pass
