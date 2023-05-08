# https://cloud.google.com/looker/docs/reference/param-view
## STRUCTURAL PARAMETERS
include: "filename_or_pattern"
## Possibly more include declarations

test: test_name {
  explore_source: explore_name {
    # Desired subparameters (described on test page)
  }
  assert: assert_statement {
    expression: Looker expression ;;
  }
  # Possibly more assert declarations
}
## Possibly more test declarations

view: view_name {
  extension: required
  extends: [view_name, view_name, ...]
  (dimension | dimension_group | measure | filter): field_name {
    # Desired field parameters (described on Field Parameters page)
  }
  # Possibly more field declarations

  set: set_name {
    fields: [field_or_set, field_or_set, ...]
  }
  # Possibly more set declarations

  drill_fields: [field_or_set, field_or_set, ...]

  # DISPLAY PARAMETERS
  label: "desired label"
  fields_hidden_by_default: yes | no

  # FILTER PARAMETERS
  suggestions: yes | no

  # QUERY PARAMETERS
  required_access_grants: [access_grant_name, access_grant_name, ...]
  sql_table_name: table_name ;;

  # DERIVED TABLE PARAMETERS
  derived_table: {
    cluster_keys: ["column_name", "column_name", ...]
    create_process: {
      sql_step: SQL query ;;
    }
    datagroup_trigger: datagroup_name
    distribution: "column_name"
    distribution_style: all | even
    explore_source: explore_name {
      # Desired subparameters (described on explore_source page)
    }
    increment_key: "column_name"
    increment_offset: N
    indexes: ["column_name", "column_name", ...]
    interval_trigger: "N (seconds | minutes | hours)"
    materialized_view: yes | no
    partition_keys: ["column_name", "column_name", ...]
    persist_for: "N (seconds | minutes | hours)"
    publish_as_db_view: yes | no
    sortkeys: ["column_name", "column_name", ...]
    sql: SQL query ;;
    sql_create: {
      SQL query ;;
    }
    sql_trigger_value: SQL query ;;
    table_compression: GZIP | SNAPPY
    table_format: PARQUET | ORC | AVRO | JSON | TEXTFILE
  }
}

## REFINEMENT PARAMETERS
view: +view_name {
  final: yes
}