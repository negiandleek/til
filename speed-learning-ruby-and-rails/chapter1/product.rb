class Tax
  def self.rate
    1.08
  end
end

module PriceHolder
  def total_price
    price * Tax.rate
  end
end

class PriceObject 
  include PriceHolder
  
  def price
    raise NotImplementedError
  end

  def echo
    print("PriceObject\n")
  end
end

class Product < PriceObject
  attr_accessor :price

  def echo
    super
    print("OrderedItem\n")
  end
end

class OrderedItem < PriceObject
  attr_accessor :unit_price, :volume

  def price
    unit_price * volume
  end
end

purchased = Product.new
purchased.price = 1000
purchased.echo()
print(purchased.total_price())

