from typing import Optional, List, Dict, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from tidy.manifest.v12.bases.file_hash import FileHash
from tidy.manifest.v12.bases.column_info import ColumnInfo
from tidy.manifest.v12.bases.docs import Docs
from tidy.manifest.v12.bases.defer_relation import DeferRelation
from tidy.manifest.v12.macros.macro_depends_on import MacroDependsOn
from tidy.manifest.v12.nodes.seeds.seed_config import SeedConfig


class Seed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    database: Optional[str] = None
    schema_: str = Field(..., alias="schema")
    name: str
    resource_type: Literal["seed"]
    package_name: str
    path: str
    original_file_path: str
    unique_id: str
    fqn: List[str]
    alias: str
    checksum: FileHash = Field(..., title="FileHash")
    config: Optional[SeedConfig] = Field(None, title="SeedConfig")
    tags: Optional[List[str]] = None
    description: Optional[str] = ""
    columns: Optional[Dict[str, ColumnInfo]] = None
    meta: Optional[Dict[str, Any]] = None
    group: Optional[str] = None
    docs: Optional[Docs] = Field(None, title="Docs")
    patch_path: Optional[str] = None
    build_path: Optional[str] = None
    unrendered_config: Optional[Dict[str, Any]] = None
    created_at: Optional[float] = None
    config_call_dict: Optional[Dict[str, Any]] = None
    unrendered_config_call_dict: Optional[Dict[str, Any]] = None
    relation_name: Optional[str] = None
    raw_code: Optional[str] = ""
    doc_blocks: Optional[List[str]] = None
    root_path: Optional[str] = None
    depends_on: Optional[MacroDependsOn] = Field(None, title="MacroDependsOn")
    defer_relation: Optional[DeferRelation] = None
