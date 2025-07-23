import collections.abc
import typing

from aviation._model import Transform


class SystemsModel:
    def __init__(self, transforms: collections.abc.Sequence[Transform[typing.Any, ...]]) -> None:
        self.transforms = transforms

    def evaluate(self, inputs: dict[str, float], output: str) -> typing.Any:  # noqa: ANN401
        # first case is if the `output` is already in the set of `inputs`
        if output in inputs:
            return inputs[output]
        # if no transform found raise error
        for transform in self.transforms:
            if transform.name == output:
                break
        else:
            message = f"No transform found that matches {output}. "
            raise ValueError(message)

        for parameter in transform.parameters:
            if parameter not in inputs:
                inputs[parameter] = self.evaluate(inputs, parameter)

        # evaluate and return the transform assosiated with the passed output
        arguments = {parameter: inputs[parameter] for parameter in transform.parameters}
        return transform(**arguments)
