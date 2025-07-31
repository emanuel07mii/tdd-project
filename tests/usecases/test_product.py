from typing import List
from uuid import UUID
from store.core.exceptions import NotFoundException

import pytest
from store.usecase.product import product_usecase
from store.schemas.product import ProductOut, ProductUpdateOut


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("fce6cc37-10b9-4a8e-a8b2-977df327001b"))
    # breakpoint()
    assert (
        err.value.message
        == "Product not found with filter: fce6cc37-10b9-4a8e-a8b2-977df327001b"
    )


async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)


async def test_usecases_update_should_return_success(product_id, product_up):
    product_up.price = 9.500
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_id):
    result = await product_usecase.delete(id=product_id)

    assert result is True


async def test_usecases_delete_should_not_found(product_id):
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("fce6cc37-10b9-4a8e-a8b2-977df327001b"))

    assert (
        err.value.message
        == "Product not found with filter: fce6cc37-10b9-4a8e-a8b2-977df327001b"
    )
