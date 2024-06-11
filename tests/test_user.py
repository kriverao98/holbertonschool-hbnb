#!/usr/bin/python3
import pytest
from Model import User, Place, Review, Amenity
from datetime import datetime
from uuid import uuid4


@pytest.fixture
def new_user():
    return User(name="John Doe", email="johndoe@gmail.com", password="123456")

def test_created_at_and_updated_at_fields(new_user):
    assert isinstance(new_user.created_at, datetime)
    assert isinstance(new_user.updated_at, datetime)
    assert new_user.created_at == new_user.updated_at

def test_relationship_integrity(new_user):
    place = Place(name="Cozy Cottage", host=new_user)
    review = Review(user=new_user, place=place, rating=5, content="Great place!")

    assert new_user in place.hosts
    assert new_user in review.users

def test_business_rule_enforcement():
    # One host per place
    user1 = User(name="John Doe", email="john@example.com")
    user2 = User(name="Jane Doe", email="jane@example.com")
    place = Place(name="Cozy Cottage", host=user1)

    with pytest.raises(Exception):
        place.host = user2

    # User uniqueness
    with pytest.raises(Exception):
        User(name="John Doe", email="john@example.com")

    # Review restrictions
    with pytest.raises(Exception):
        Review(user=user1, place=place, rating=6, content="Awesome place!")

def test_user_creation_validation():
    # Valid input
    user = User(name="John Doe", email="john@example.com")
    assert user.name == "John Doe"
    assert user.email == "john@example.com"

    # Invalid email format
    with pytest.raises(Exception):
        User(name="Jane Doe", email="invalid_email")

    # Missing required fields
    with pytest.raises(Exception):
        User(email="missing_name@example.com")

def test_unique_email_constraint():
    User(name="John Doe", email="john@example.com")
    with pytest.raises(Exception):
        User(name="Jane Doe", email="john@example.com")