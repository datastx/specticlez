explore: orders {
  view_name: order
  label: "Orders"
  description: "Explore for order data"
  
  join: customer {
    type: left_outer
    sql_on: ${orders.customer_id} = ${customer.id}
  }
  
  join: product {
    type: inner
    relationship: many_to_one
    sql_on: ${orders.product_id} = ${product.id}
  }
  
  dimension_group: order_date {
    type: time
    timeframes: [time, date, week, month, quarter, year]
    sql: ${TABLE}.order_date
  }
  
  dimension: customer_name {
    type: string
    sql: ${customer.name} ;;
  }
  
  measure: total_sales {
    type: sum
    sql: ${TABLE}.sales_amount ;;
  }
  
  filter: order_status {
    type: string
    values: [pending, shipped, delivered]
    sql: ${TABLE}.status ;;
  }
  
  access_grant: {
    type: all
  }
}
