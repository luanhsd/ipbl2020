
exports.up = function (knex) {
    return knex.schama.createTable('contacts', function (table) {
        table.increments('id').primary()
        table.integer('physicianId').unsigned().notNullable()
        table.string('type').notNullable()
        table.string('contact').notNullable()
        table.foreign('physicianId').references('id').inTable('physicians')
    })
};

exports.down = function (knex) {
    return knex.schema.dropTable('contacts')
};
