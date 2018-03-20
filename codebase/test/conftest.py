import pytest
from contextlib import contextmanager

@pytest.fixture(scope='module', params=[x for x in range(0, 10)])
def anyint(request):
  yield request.param
  print('finished:', request.param)
