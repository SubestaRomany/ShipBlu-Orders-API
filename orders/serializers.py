from rest_framework import serializers
from .models import Customer, Order, OrderTrackingEvent

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderTrackingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTrackingEvent
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    tracking_events = OrderTrackingEventSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_tracking_number(self, value):
        if self.instance is None and Order.objects.filter(tracking_number=value).exists():
            raise serializers.ValidationError("Tracking number must be unique.")
        return value

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer, _ = Customer.objects.get_or_create(name=customer_data.get('name'), defaults=customer_data)
        order = Order.objects.create(customer=customer, **validated_data)

        OrderTrackingEvent.objects.create(
            order=order,
            status=order.status,
            comment="Order created"
        )
        return order

    def update(self, instance, validated_data):
        old_status = instance.status
        new_status = validated_data.get('status', old_status)

        if 'status' in validated_data:
            if old_status == 'CREATED' and new_status == 'PICKED':
                pass
            elif old_status == 'PICKED' and new_status == 'DELIVERED':
                pass
            elif old_status == new_status:
                pass
            else:
                raise serializers.ValidationError("Invalid status transition.")

        updated_instance = super().update(instance, validated_data)

        if old_status != new_status:
            OrderTrackingEvent.objects.create(
                order=instance,
                status=new_status,
                comment=f"Status changed from {old_status} to {new_status}"
            )

        return updated_instance

