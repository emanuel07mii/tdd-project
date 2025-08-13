from typing import List

import pytest
from tests.factories import product_data
from fastapi import status
from unittest.mock import AsyncMock
from pymongo.errors import PyMongoError


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }.items() <= content.items()


@pytest.mark.asyncio
async def test_controller_create_should_return_error_on_duplicate(client, products_url):
    # Primeira inserção → sucesso
    response_1 = await client.post(products_url, json=product_data())
    assert response_1.status_code == status.HTTP_201_CREATED

    # Segunda inserção com mesmo "name" → erro
    response_2 = await client.post(products_url, json=product_data())
    assert response_2.status_code == status.HTTP_400_BAD_REQUEST
    assert (
        response_2.json()["detail"]
        == "Erro de integridade: Produto duplicado ou dados inválidos"
    )


@pytest.mark.asyncio
async def test_controller_create_should_return_error_on_db_failure(
    client, products_url, monkeypatch
):
    from store.usecases.product import ProductUsecase

    mock_collection = AsyncMock()
    mock_collection.insert_one.side_effect = PyMongoError("Erro ao inserir no banco")

    def fake_init(self):
        self.collection = mock_collection

    monkeypatch.setattr(ProductUsecase, "__init__", fake_init)

    response = await client.post(products_url, json=product_data())
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert "Erro ao inserir no banco" in response.json()["detail"]


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}fce6cc37-10b9-4a8e-a8b2-977df327001b")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: fce6cc37-10b9-4a8e-a8b2-977df327001b"
    }


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_success(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_patch_should_return_success(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"price": "8.300"}
    )

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.300",
        "status": True,
    }


async def test_controller_patch_should_return_not_found(client, products_url):
    response = await client.patch(
        f"{products_url}fce6cc37-10b9-4a8e-a8b2-977df327001b", json={"price": "8.300"}
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: fce6cc37-10b9-4a8e-a8b2-977df327001b"
    }


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}fce6cc37-10b9-4a8e-a8b2-977df327001b"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: fce6cc37-10b9-4a8e-a8b2-977df327001b"
    }
