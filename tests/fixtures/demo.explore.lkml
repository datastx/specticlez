# https://cloud.google.com/looker/docs/reference/param-explore
## STRUCTURAL PARAMETERS
explore: explore_name {
  extension: required
  extends: [explore_name, explore_name]
  fields: [field_or_set, field_or_set]
  tags: ["string1", "string2"]

  # DISPLAY PARAMETERS
  description: "Description I want"
  group_label: "Label to use as a heading in the Explore menu"
  hidden:  yes #yes | no
  label: "desired label"
  query: query_name {
    dimensions: [dimension1, dimension2 ]
    measures: [measure1, measure2]
    label: "Display Name in Field Picker"
    description: "Information about this query"
    pivots: [dimension1, dimension2]
    sorts: [field1: asc, field2: desc]
    filters: [field1: "value1", field2: "value2"]
    limit: 100
  }
  view_label: "Field picker heading I want for the Explore's fields"

  # FILTER PARAMETERS
  access_filter: {
    field: fully_scoped_field
    user_attribute: user_attribute_name
  }
  # Possibly more access_filter declarations
  always_filter: {
    filters: [field_name: "filter expression", field_name: "filter expression"]
  }
  case_sensitive: yes # yes | no
  conditionally_filter: {
    filters: [field_name: "filter expression", field_name: "filter expression"]
    unless: [field_name, field_name]
  }
  # TODO: figure out how to do this after we get
  # this test file working
  # sql_always_having: SQL HAVING condition ;;
  # sql_always_where: SQL WHERE condition ;;

  # JOIN PARAMETERS
  always_join: [view_name_to_use, view_name_to_use]
  join: join_name {
    # DISPLAY PARAMETERS
    view_label: "desired label for the view"

    # JOIN PARAMETERS
    fields: [field_or_set, field_or_set]
    foreign_key: dimension_name
    from: view_name_to_use
    outer_only: yes # no | yes
    relationship: one_to_one # many_to_one | many_to_many | one_to_many | one_to_one
    required_joins: [view_name_to_use, view_name_to_use]
    # TODO: figure out how to do this after we get
    # this test file working
    # sql_on: SQL ON clause ;;
    # sql_table_name: table_name ;;
    type: inner #left_outer | cross | full_outer | inner

    # QUERY PARAMETERS
    required_access_grants: [access_grant_name, access_grant_name]
    # TODO: figure out how to do this after we get
    # this test file working
    # sql_where: SQL WHERE condition ;;
  }
  # Possibly more join declarations

  # QUERY PARAMETERS
  cancel_grouping_fields: [fully_scoped_field, fully_scoped_field]
  from: view_name_to_use
  persist_for: "1 hours"
  persist_with: datagroup_name
  required_access_grants: [access_grant_name, access_grant_name]
  sql_table_name: table_name ;;
  symmetric_aggregates: no
  view_name: view_name_to_use

  # AGGREGATE TABLE PARAMETERS
  aggregate_table: order_summary {
    query: {
      dimensions: [order.created_month, product.category]
      measures: [order.total_revenue, order.total_items]
      timeframes: [created_month]
      filters: [order.status: "complete"]
    }
    materialization: {
      datagroup_trigger: order_datagroup
    }
  }
  }
  # Possibly more aggregate_table declarations



## REFINEMENT PARAMETERS
explore: +explore_name {
  final: yes
}