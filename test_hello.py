"""
Unit tests for hello.py
"""
import pytest
from hello import greet


def test_greet_default():
    """Test greeting with default name."""
    assert greet() == "Hello, World!"


def test_greet_custom():
    """Test greeting with custom name."""
    assert greet("Alice") == "Hello, Alice!"
