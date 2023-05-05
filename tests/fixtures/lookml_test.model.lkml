explore: order_items_explore {
  join: orders {
    sql_on: ${order_items.order_id} = ${orders.id} ;;
    relationship: many_to_one
  }

  join: products {
    sql_on: ${order_items.product_id} = ${products.id} ;;
    relationship: many_to_one
  }

  join: customers {
    sql_on: ${orders.customer_id} = ${customers.id} ;;
    relationship: many_to_one
  }
}
