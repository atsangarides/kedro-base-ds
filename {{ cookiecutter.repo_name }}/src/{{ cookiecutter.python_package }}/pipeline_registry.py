"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, node

# from .nodes.raw import f
# from .nodes.intermediate import f
# from .nodes.primary import f
# from .nodes.feature import f
# from .nodes.model_input import f
# from .nodes.models import f
# from .nodes.model_output import f
# from .nodes.reporting import f


def create_pipelines() -> Dict[str, Pipeline]:
    """Create the project's pipeline.
    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    # Execute pipelines
    # raw_pipeline = _create_raw_layer()
    # intermediate_pipeline = _create_intermediate_layer()
    # primary_pipeline = _create_primary_layer()
    # feature_pipeline = _create_feature_layer()
    # model_input_pipeline = _create_model_input_layer()
    # models_pipeline = _create_models_layer()
    # model_output_pipeline = _create_model_output_layer()
    # reporting_pipeline = _create_reporting_layer()

    # Build entire pipeline
    base_pipeline = Pipeline([
        # raw_pipeline,
        # intermediate_pipeline,
        # primary_pipeline,
        # feature_pipeline,
        # model_input_pipeline,
        # models_pipeline,
        # model_output_pipeline,
        # reporting_pipeline

    ])

    return {
        "__default__": base_pipeline,
    }

#
# def _create_raw_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             outputs="raw-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_raw")
#

# def _create_intermediate_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             inputs=["raw-dataset", "parameters"],
#             outputs="int-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_int")
#
#
# def _create_primary_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             inputs=["int-dataset", "parameters"],
#             outputs="prim-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_prim")
#
#
# def _create_feature_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             inputs=["prim-dataset", "parameters"],
#             outputs="feat-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_feat")
#
#
# def _create_model_input_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             inputs=["feat-dataset", "parameters"],
#             outputs="mi-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_mi")
#
#
# def _create_models_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             inputs=["mi-dataset", "parameters"],
#             outputs="mod-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_mod")
#
#
# def _create_model_output_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             inputs=["mod-dataset", "parameters"],
#             outputs="mo-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_mo")
#
#
# def _create_reporting_layer() -> Pipeline:
#
#     all_nodes = [
#         node(
#             func=f,
#             inputs=["mo-dataset", "parameters"],
#             outputs="re-dataset"
#         )
#     ]
#
#     return Pipeline(all_nodes, tags="to_re")

