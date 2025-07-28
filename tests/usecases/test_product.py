from uuid import UUID
from store.core.exceptions import NotFoundException

import pytest
from store.usecase.product import product_usecase
from store.schemas.product import ProductOut


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
