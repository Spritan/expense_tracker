"""
This type stub file was generated by pyright.
"""

import proto
from typing import MutableSequence
from google.protobuf import struct_pb2

"""
This type stub file was generated by pyright.
"""
__protobuf__ = ...
class PredictRequest(proto.Message):
    r"""Request message for
    [PredictionService.Predict][google.ai.generativelanguage.v1beta.PredictionService.Predict].

    Attributes:
        model (str):
            Required. The name of the model for prediction. Format:
            ``name=models/{model}``.
        instances (MutableSequence[google.protobuf.struct_pb2.Value]):
            Required. The instances that are the input to
            the prediction call.
        parameters (google.protobuf.struct_pb2.Value):
            Optional. The parameters that govern the
            prediction call.
    """
    model: str = ...
    instances: MutableSequence[struct_pb2.Value] = ...
    parameters: struct_pb2.Value = ...


class PredictResponse(proto.Message):
    r"""Response message for [PredictionService.Predict].

    Attributes:
        predictions (MutableSequence[google.protobuf.struct_pb2.Value]):
            The outputs of the prediction call.
    """
    predictions: MutableSequence[struct_pb2.Value] = ...


__all__ = tuple(sorted(__protobuf__.manifest))
