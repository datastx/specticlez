view: order_items {
  sql_table_name: public.order_items;;

  dimension: id {
    type: number
    sql: ${TABLE}.id;;
    primary_key: yes
  }

  dimension: order_id {
    type: number
    sql: ${TABLE}.order_id;;
  }

  dimension: product_id {
    type: number
    sql: ${TABLE}.product_id;;
  }

  dimension: quantity {
    type: number
    sql: ${TABLE}.quantity;;
  }

  dimension: sale_price {
    type: number
    sql: ${TABLE}.sale_price;;
  }

  dimension: created_at {
    type: time
    timeframes: [
      raw,
      time,
      date,
      week,
      month,
      quarter,
      year
    ]
    sql: ${TABLE}.created_at;;
  }

  measure: total_revenue {
    type: sum
    value_format: "$0,0.00"
  }
}