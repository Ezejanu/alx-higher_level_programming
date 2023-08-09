#!/usr/bin/python3
"""Defines a matrix multiplication function"""
import numpy as npy

def lazy_matrix_mul(m_a, m_b):
    """Returns the output of multiplying two matrices"""

    return (npy.matmul(m_a, m_b))
