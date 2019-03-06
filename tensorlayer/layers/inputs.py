#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
import tensorlayer as tl

from tensorlayer.layers.core import Layer, LayerNode
# from tensorlayer.layers.core import LayersConfig

from tensorlayer import logging

__all__ = [
    'Input',
    'InputLayer'
]


class InputLayer(Layer):
    """
    The :class:`Input` class is the starting layer of a neural network.

    Parameters
    ----------
    shape : tuple (int)
        Including batch size.
    name : None or str
        A unique layer name.

    """

    def __init__(self, shape, dtype=tf.float32, name=None):  #'input'):
        # super(InputLayer, self).__init__(prev_layer=inputs, name=name)
        super(InputLayer, self).__init__(name)

        logging.info("Input  %s: %s" % (self.name, str(shape)))
        self.shape = shape # shape is needed in __repr__

        shape_without_none = [_ if _ is not None else 1 for _ in shape]
        # self.outputs = self.forward(tl.initializers.random_normal()(shape_without_none))
        self.outputs = self.forward(tl.initializers.ones()(shape_without_none, dtype=dtype))

        self._built = True

        self._add_node(self.outputs, self.outputs)

    def __repr__(self):
        s = 'Input(shape=%s' % str(self.shape)
        if self.name is not None:
            s += (', name=\'%s\'' % self.name)
        s += ')'
        return s

    def __call__(self, inputs):
        return super(InputLayer, self).__call__(prev_layer=inputs)

    def build(self, inputs_shape):
        # FIXME: documentation need double check
        """
        no weights to define
        """
        pass

    def forward(self, inputs):
        # FIXME: documentation need double check
        """
        Parameters
        ----------
        inputs : input tensor
            The input of a network.
        is_train: bool
            train (True) or test (False)
        """
        return inputs


def Input(shape, dtype=tf.float32, name=None):
    input_layer = InputLayer(shape, dtype=dtype, name=name)
    outputs = input_layer._nodes[0].out_tensors[0]
    return outputs