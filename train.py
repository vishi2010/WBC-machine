import tensorflow as tf
from model import build_wbc_model
import os

def preprocess(image, label):
    image = tf.cast(image, tf.float32)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return image, label

train_ds = tf.keras.utils.image_dataset_from_directory(
    'YOUR_PATH_TO_TRAINING_DATASET',
    image_size=(224, 224),
    batch_size=32,
    shuffle=True,
    seed=42
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    'YOUR_PATH_TO_VALIDATION_DATASET',
    image_size=(224, 224),
    batch_size=32,
    seed=42
)

train_ds = train_ds.map(
    preprocess, num_parallel_calls=tf.data.AUTOTUNE
).shuffle(10000).prefetch(tf.data.AUTOTUNE)

val_ds = val_ds.map(
    preprocess, num_parallel_calls=tf.data.AUTOTUNE
).prefetch(tf.data.AUTOTUNE)

model = build_wbc_model(num_classes=4)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.00001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()
os.makedirs('model', exist_ok=True)

callbacks = [
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_accuracy',
        factor=0.5,
        patience=3,
        verbose=1,
        min_lr=1e-8
    ),
    tf.keras.callbacks.EarlyStopping(
        monitor='val_accuracy',
        patience=8,
        restore_best_weights=True,
        verbose=1
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'model/best_model.keras',
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    )
]

model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=30,
    callbacks=callbacks
)

model.save('model/wbc_model.keras')
print("Done!")
