from sympy.physics.quantum.qapply import qapply as sympy_qapply

from quantpy.sympy.executor._base_quantum_executor import BaseQuantumExecutor


class SymPyExecutor(BaseQuantumExecutor):
    def __init__(self):
        super().__init__()

    def execute(self, circuit, **options):
        return sympy_qapply(circuit, **options)
