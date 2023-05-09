# https://cloud.google.com/looker/docs/reference/param-view
## STRUCTURAL PARAMETERS
include: "filename_or_pattern"
## Possibly more include declarations

# TODO: build this out
test: historic_revenue_is_accurate {
  explore_source: orders {
    column: total_revenue {
      field: orders.total_revenue
    }
    filters: [orders.created_date: "2017"]
  }
  assert: revenue_is_expected_value {
    expression: ${orders.total_revenue} = 626000 ;;
  }
}
## Possibly more test declarations

view: view_name_for_use {
  extension: required
  extends: [view_name_for_use, view_name_for_use]
  # https://cloud.google.com/looker/docs/reference/param-field
  dimension : dimension_name {

    # ACTION AND LINKING PARAMETERS
    action: {
      label: "Label to Appear in Action Menu"
      url: "https://example.com/posts"
      icon_url: "https://looker.com/favicon.ico"
      form_url: "https://example.com/ping/{{ value }}/form.json"
      param: {
        name: "name string"
        value: "value string"
      }
      form_param: {
        name: "name string"
        type: textarea 
        label: "possibly-localized-string"
        option: {
          name: "name string"
          label: "possibly-localized-string"
        }
        required: yes # yes | no
        description: "possibly-localized-string"
        default: "string"
      }
      user_attribute_param: {
        user_attribute: user_attribute_name
        name: "name_for_json_payload"
      }
    }
    drill_fields: [field_or_set, field_or_set]
    tags: ["string1", "string2"]
    link: {
      label: "desired label name;"
      url: "desired_url"
      icon_url : "url_of_an_image_file"
    }
    # Possibly more link definitions

    # DISPLAY PARAMETERS
    alias: [old_field_name, old_field_name]
    alpha_sort: no # yes | no
    description: "description string"
    group_label: "desired group label name"
    group_item_label: "label to use under the group label in the field picker"
    hidden: yes # yes | no
    label: "desired label name"
    label_from_parameter: parameter_name
    order_by_field: dimension_name # dimension_name | dimension_group_name | measure_name
    style: classic # classic | interval | integer | relational
    view_label: "desired label name"

    # FILTER PARAMETERS
    can_filter: yes # yes | no
    case_sensitive: no #yes | no

    
    # Possibly more allowed_value definitions
    bypass_suggest_restrictions: yes # yes | no
    full_suggestions: no #yes | no
    suggest_dimension: dimension_name
    suggest_explore: explore_name
    suggest_persist_for: "5 hours" #"N (seconds | minutes | hours)"
    suggestable: no # yes | no
    suggestions: ["suggestion string", "suggestion string"]

    # QUERY PARAMETERS
    convert_tz: yes #yes | no
    datatype: epoch # epoch | timestamp | datetime | date | yyyymmdd
    fanout_on: repeated_record_name
    primary_key: no # yes | no
    required_access_grants: [access_grant_name, access_grant_name]
    required_fields: [field_name, field_name]

    # VALUE AND FORMATTING PARAMETERS
    case: {
      when: {
        sql: SQL condition ;;
        label: "value"
      }
      # Possibly more when statements
    }
    # TODO: REVIEW THIS LOGIC
    end_location_field: dimension_name
    html: HTML expression using Liquid template elements ;;
    sql: SQL expression to generate the field value ;;
    sql_end: SQL expression indicating the end time of a duration ;;
    sql_latitude: SQL expression to generate a latitude ;;
    sql_longitude: SQL expression to generate a longitude ;;
    sql_start: SQL expression indicating the start time of a duration ;;
    start_location_field: dimension_name
    tiers: [N, N]
    string_datatype: unicode # For a dimension field
    units: feet # feet | kilometers | meters | miles | nautical_miles | yards
    value_format: "excel-style formatting string"
    value_format_name: format_name

    # VISUALIZATION PARAMETERS
    allow_fill: no # yes | no
    map_layer_name: name_of_map_layer
    }

  # Possibly more field declarations

  set: set_name {
    fields: [field_or_set, field_or_set]
  }
  # Possibly more set declarations

  drill_fields: [field_or_set, field_or_set]

  # DISPLAY PARAMETERS
  label: "desired label"
  fields_hidden_by_default: yes # yes | no

  # FILTER PARAMETERS
  suggestions: no # yes | no

  # QUERY PARAMETERS
  required_access_grants: [access_grant_name, access_grant_name]
  sql_table_name: table_name ;;

  # DERIVED TABLE PARAMETERS
  derived_table: {
    cluster_keys: ["column_name", "column_name"]
    create_process: {
      sql_step: SQL query ;;
    }
    datagroup_trigger: datagroup_name
    distribution: "column_name"
    distribution_style: all # all | even
    explore_source: explore_name {
      # Desired subparameters (described on explore_source page)
    }
    increment_key: "column_name"
    increment_offset: N
    indexes: ["column_name", "column_name"]
    interval_trigger: "3 minutes" # "N (seconds | minutes | hours)"
    materialized_view: no # yes | no
    partition_keys: ["column_name", "column_name"]
    persist_for: "8 seconds" # "N (seconds | minutes | hours)"
    publish_as_db_view: no # yes | no
    sortkeys: ["column_name", "column_name"]
    sql: SQL query ;;
    sql_create: {
      SQL query ;;
    }
    sql_trigger_value: SQL query ;;
    table_compression: GZIP # GZIP | SNAPPY
    table_format: PARQUET # PARQUET | ORC | AVRO | JSON | TEXTFILE
  }
}

## REFINEMENT PARAMETERS
view: +view_name_for_use {
  final: yes
}